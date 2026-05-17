#!/usr/bin/env python3
"""
Quick validation script for skills - minimal version
"""

import sys
import os
import re
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit(
        "Error: PyYAML is required but not installed.\n"
        "Install it with: pip install pyyaml\n"
        "Or: py -m pip install pyyaml"
    )

def check_references(skill_path, content):
    """Check that local file references in SKILL.md are reachable.

    Checks markdown links and inline backtick references under
    scripts/, references/, and assets/ directories.
    """
    # Remove fenced code blocks
    cleaned = re.sub(r'```[\s\S]*?```', '', content)

    bad_refs = []
    checked = set()  # Dedup repeated references

    def add_issue(path, context):
        target = skill_path / path
        if path not in checked:
            checked.add(path)
            if not target.exists():
                bad_refs.append(f"  - {path} ({context})")

    # Check markdown links: [text](path) and ![alt](path)
    for m in re.finditer(r'\[([^\]]*)\]\(([^\)]+)\)', cleaned):
        path = m.group(2).split('#')[0].split('?')[0].strip()
        path = re.sub(r'^\./', '', path)  # Normalize ./ prefix
        if path.startswith(('scripts/', 'references/', 'assets/')):
            add_issue(path, "markdown link")

    # Check inline backtick references: `path`
    first_word = re.compile(r'`([^`]+)`')
    for m in first_word.finditer(cleaned):
        path = m.group(1).strip().split()[0]  # First word, drop args
        if path.startswith(('scripts/', 'references/', 'assets/')):
            add_issue(path, "inline reference")

    return bad_refs


def validate_skill(skill_path):
    """Basic validation of a skill"""
    skill_path = Path(skill_path).resolve()

    # Check SKILL.md exists
    skill_md = skill_path / 'SKILL.md'
    if not skill_md.exists():
        return False, "SKILL.md not found"

    # Read and validate frontmatter
    content = skill_md.read_text(encoding='utf-8')
    if not content.startswith('---'):
        return False, "No YAML frontmatter found"

    # Extract frontmatter
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return False, "Invalid frontmatter format"

    frontmatter_text = match.group(1)

    # Parse YAML frontmatter
    try:
        frontmatter = yaml.safe_load(frontmatter_text)
        if not isinstance(frontmatter, dict):
            return False, "Frontmatter must be a YAML dictionary"
    except yaml.YAMLError as e:
        return False, f"Invalid YAML in frontmatter: {e}"

    # Define allowed properties
    ALLOWED_PROPERTIES = {'name', 'description', 'license', 'allowed-tools', 'metadata', 'compatibility'}

    # Check for unexpected properties (excluding nested keys under metadata)
    unexpected_keys = set(frontmatter.keys()) - ALLOWED_PROPERTIES
    if unexpected_keys:
        return False, (
            f"Unexpected key(s) in SKILL.md frontmatter: {', '.join(sorted(unexpected_keys))}. "
            f"Allowed properties are: {', '.join(sorted(ALLOWED_PROPERTIES))}"
        )

    # Check required fields
    if 'name' not in frontmatter:
        return False, "Missing 'name' in frontmatter"
    if 'description' not in frontmatter:
        return False, "Missing 'description' in frontmatter"

    # Extract name for validation
    name = frontmatter.get('name', '')
    if not isinstance(name, str):
        return False, f"Name must be a string, got {type(name).__name__}"
    name = name.strip()
    if not name:
        return False, "Name must not be empty"
    if name:
        # Check naming convention (kebab-case: lowercase with hyphens)
        if not re.match(r'^[a-z0-9-]+$', name):
            return False, f"Name '{name}' should be kebab-case (lowercase letters, digits, and hyphens only)"
        if name.startswith('-') or name.endswith('-') or '--' in name:
            return False, f"Name '{name}' cannot start/end with hyphen or contain consecutive hyphens"
        # Check name length (max 64 characters per spec)
        if len(name) > 64:
            return False, f"Name is too long ({len(name)} characters). Maximum is 64 characters."

    # Check directory name matches name field
    dir_name = skill_path.name
    if dir_name != name:
        return False, f"Directory name '{dir_name}' does not match skill name '{name}'"

    # Extract and validate description
    description = frontmatter.get('description', '')
    if not isinstance(description, str):
        return False, f"Description must be a string, got {type(description).__name__}"
    description = description.strip()
    if description:
        # Check for angle brackets
        if '<' in description or '>' in description:
            return False, "Description cannot contain angle brackets (< or >)"
        # Check description length (max 1024 characters per spec)
        if len(description) > 1024:
            return False, f"Description is too long ({len(description)} characters). Maximum is 1024 characters."

    # Validate compatibility field if present (optional)
    compatibility = frontmatter.get('compatibility', '')
    if compatibility:
        if not isinstance(compatibility, str):
            return False, f"Compatibility must be a string, got {type(compatibility).__name__}"
        if len(compatibility) > 500:
            return False, f"Compatibility is too long ({len(compatibility)} characters). Maximum is 500 characters."

    # Check local file references in SKILL.md
    ref_issues = check_references(skill_path, content)
    if ref_issues:
        msg = "Broken references in SKILL.md:\n" + "\n".join(ref_issues)
        return False, msg

    return True, "Skill is valid!"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python quick_validate.py <skill_directory>")
        sys.exit(1)
    
    valid, message = validate_skill(sys.argv[1])
    print(message)
    sys.exit(0 if valid else 1)
