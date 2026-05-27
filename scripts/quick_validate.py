#!/usr/bin/env python3
"""
Quick validation script for skills - returns structured result without exit codes.
"""

import sys
import re
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Error: PyYAML is required but not installed.")
    print("Install it with: pip install pyyaml")
    print("Or: py -m pip install pyyaml")
    sys.exit(1)  # 保留依赖缺失的退出，因为无法运行

def check_references(skill_path, content):
    """Check that local file references in SKILL.md are reachable."""
    cleaned = re.sub(r'```[\s\S]*?```', '', content)
    bad_refs = []
    checked = set()

    def add_issue(path, context):
        target = skill_path / path
        if path not in checked:
            checked.add(path)
            if not target.exists():
                bad_refs.append(f"  - {path} ({context})")

    # Markdown links
    for m in re.finditer(r'\[([^\]]*)\]\(([^\)]+)\)', cleaned):
        path = m.group(2).split('#')[0].split('?')[0].strip()
        path = re.sub(r'^\./', '', path)
        if path.startswith(('scripts/', 'references/', 'assets/')):
            add_issue(path, "markdown link")

    # Inline backtick references
    first_word = re.compile(r'`([^`]+)`')
    for m in first_word.finditer(cleaned):
        path = m.group(1).strip().split()[0]
        if path.startswith(('scripts/', 'references/', 'assets/')):
            add_issue(path, "inline reference")

    return bad_refs

def check_recommendations(frontmatter, content, skill_path):
    """Return a list of warning messages for non-critical improvements.

    All content checks operate on cleaned text (code blocks removed)
    to avoid false positives from template examples inside fenced blocks.
    Section matching is content-signature-based, not exact header names:
    - Rationalizations: | Rationalization | Reality | table anywhere
    - Gotchas: | ID | Issue / Symptom | Fix | table anywhere
    - Verification: | Check | Evidence | table anywhere
    - Workflow steps: Phase/Step N headers or plain numbered lists
    """
    cleaned = re.sub(r'```[\s\S]*?```', '', content)
    warnings = []

    # 1. description contains "use when"
    desc = frontmatter.get('description', '')
    if desc and 'use when' not in desc.lower():
        warnings.append("Recommendation: description should include 'Use when' trigger conditions")

    # 2. Rationalization table (content-signature, not header-name)
    if '| Rationalization | Reality |' not in cleaned:
        warnings.append(
            "Recommendation: Consider adding a rationalization table "
            "(| Rationalization | Reality |) — can live inside Core Principles, Top Reminders, or any section"
        )

    # 3. Gotchas table (content-signature, not header-name)
    has_gotchas_table = bool(re.search(r'\|.*ID.*Issue.*Symptom.*Fix.*\|', cleaned))
    if not has_gotchas_table:
        warnings.append(
            "Recommendation: Consider adding a Gotchas/Guardrails table "
            "(| ID | Issue / Symptom | Fix |)"
        )

    # 4. Verification table (content-signature, not header-name)
    has_verification_table = bool(re.search(r'\|.*Check.*Evidence.*\|', cleaned))
    if not has_verification_table:
        warnings.append(
            "Recommendation: Consider adding a Verification table "
            "(| Check | Evidence |)"
        )

    # 5. Forbidden auxiliary files
    forbidden = ['README.md', 'CHANGELOG.md', 'INSTALLATION_GUIDE.md']
    for f in forbidden:
        if (skill_path / f).exists():
            warnings.append(f"Recommendation: Remove auxiliary file {f} – not needed for skills")

    # 6. Numbered steps/processes in Workflow-like sections
    workflow_match = re.search(r'## [^#\n]*[Ww]orkflow', cleaned)
    if workflow_match:
        rest = cleaned[workflow_match.start():]
        section_match = re.search(r'(## [^#\n]*[Ww]orkflow.*?)(?=\n## |\Z)', rest, re.DOTALL)
        if section_match:
            section_text = section_match.group(1)
            has_plain = bool(re.search(r'\n\d+\.', section_text))
            has_phase = bool(re.search(r'###.*[Pp]hase\s+\d+', section_text))
            has_step = bool(re.search(r'#+\s*[Ss]tep\s+\d+', section_text))
            if not (has_plain or has_phase or has_step):
                warnings.append(
                    "Recommendation: Workflow section should use numbered steps "
                    "(e.g., 1., Phase 1, Step 1)"
                )

    return warnings

def validate_skill(skill_path):
    """
    Validate a skill. Returns a dictionary with keys:
      - valid: bool
      - message: str (error message if invalid, else "Skill is valid!")
      - warnings: list of str
    """
    skill_path = Path(skill_path).resolve()
    skill_md = skill_path / 'SKILL.md'
    if not skill_md.exists():
        return {"valid": False, "message": "SKILL.md not found", "warnings": []}

    content = skill_md.read_text(encoding='utf-8')
    if not content.startswith('---'):
        return {"valid": False, "message": "No YAML frontmatter found", "warnings": []}

    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {"valid": False, "message": "Invalid frontmatter format", "warnings": []}

    frontmatter_text = match.group(1)
    try:
        frontmatter = yaml.safe_load(frontmatter_text)
        if not isinstance(frontmatter, dict):
            return {"valid": False, "message": "Frontmatter must be a YAML dictionary", "warnings": []}
    except yaml.YAMLError as e:
        return {"valid": False, "message": f"Invalid YAML in frontmatter: {e}", "warnings": []}

    ALLOWED_PROPERTIES = {'name', 'description', 'license', 'allowed-tools', 'metadata', 'compatibility'}
    unexpected_keys = set(frontmatter.keys()) - ALLOWED_PROPERTIES
    if unexpected_keys:
        return {"valid": False,
                "message": f"Unexpected key(s) in SKILL.md frontmatter: {', '.join(sorted(unexpected_keys))}. "
                           f"Allowed properties are: {', '.join(sorted(ALLOWED_PROPERTIES))}",
                "warnings": []}

    if 'name' not in frontmatter:
        return {"valid": False, "message": "Missing 'name' in frontmatter", "warnings": []}
    if 'description' not in frontmatter:
        return {"valid": False, "message": "Missing 'description' in frontmatter", "warnings": []}

    name = frontmatter.get('name', '')
    if not isinstance(name, str):
        return {"valid": False, "message": f"Name must be a string, got {type(name).__name__}", "warnings": []}
    name = name.strip()
    if not name:
        return {"valid": False, "message": "Name must not be empty", "warnings": []}
    if not re.match(r'^[a-z0-9-]+$', name):
        return {"valid": False,
                "message": f"Name '{name}' should be kebab-case (lowercase letters, digits, and hyphens only)",
                "warnings": []}
    if name.startswith('-') or name.endswith('-') or '--' in name:
        return {"valid": False,
                "message": f"Name '{name}' cannot start/end with hyphen or contain consecutive hyphens",
                "warnings": []}
    if len(name) > 64:
        return {"valid": False,
                "message": f"Name is too long ({len(name)} characters). Maximum is 64 characters.",
                "warnings": []}

    dir_name = skill_path.name
    if dir_name != name:
        return {"valid": False,
                "message": f"Directory name '{dir_name}' does not match skill name '{name}'",
                "warnings": []}

    description = frontmatter.get('description', '')
    if not isinstance(description, str):
        return {"valid": False, "message": f"Description must be a string, got {type(description).__name__}", "warnings": []}
    description = description.strip()
    if description:
        if '<' in description or '>' in description:
            return {"valid": False, "message": "Description cannot contain angle brackets (< or >)", "warnings": []}
        if len(description) > 1024:
            return {"valid": False,
                    "message": f"Description is too long ({len(description)} characters). Maximum is 1024 characters.",
                    "warnings": []}

    compatibility = frontmatter.get('compatibility', '')
    if compatibility:
        if not isinstance(compatibility, str):
            return {"valid": False, "message": f"Compatibility must be a string, got {type(compatibility).__name__}", "warnings": []}
        if len(compatibility) > 500:
            return {"valid": False,
                    "message": f"Compatibility is too long ({len(compatibility)} characters). Maximum is 500 characters.",
                    "warnings": []}

    ref_issues = check_references(skill_path, content)
    if ref_issues:
        msg = "Broken references in SKILL.md:\n" + "\n".join(ref_issues)
        return {"valid": False, "message": msg, "warnings": []}

    warnings = check_recommendations(frontmatter, content, skill_path)

    return {"valid": True, "message": "Skill is valid!", "warnings": warnings}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python quick_validate.py <skill_directory>")
        print("Return value: a JSON-like dictionary printed to stdout.")
        sys.exit(1)

    result = validate_skill(sys.argv[1])
    # 简单打印字典（可改用 json.dumps 如果需要）
    print(result)
    # 不再使用 sys.exit(1) 来指示失败；调用方根据 result["valid"] 自行判断
