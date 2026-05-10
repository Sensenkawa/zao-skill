# Skill Anatomy Reference

> Load this when you need to understand the complete structure specification of a skill — SKILL.md format, directory layout, resource organization, and naming conventions.

## SKILL.md

### Frontmatter (required)

YAML at the top, enclosed in `---`:

```yaml
---
name: my-skill
description: >-
  What this skill does and when to use it. Include specific triggers
  like "Use when working with .pdf files for: (1) Rotating, (2) Extracting text"
license: Optional license identifier
compatibility: Optional environment requirements (rarely needed)
---
```

**Required fields**: `name` (kebab-case, max 64 chars), `description` (max 1024 chars, no angle brackets)
**Optional fields**: `license`, `compatibility`, `metadata`

The `description` is the primary trigger mechanism — the assistant reads it to decide if the skill should activate. Put ALL "when to use" info here, NOT in the body.

### Body (required)

Markdown content loaded only after the skill triggers. Keep under 500 lines. Use imperative/infinitive form.

## Directory Layout

```
skill-name/
├── SKILL.md          (required)
├── scripts/          (optional) - Executable code
├── references/       (optional) - Documentation loaded on demand
└── assets/           (optional) - Files used in output, not in context
```

Do NOT create auxiliary files: README, CHANGELOG, INSTALLATION_GUIDE, etc.

## scripts/

Executable code (Python, Bash, etc.) for deterministic or frequently repeated tasks.

- **When to include**: Code that would be rewritten repeatedly, or needs deterministic reliability
- **Example**: `scripts/rotate_pdf.py` for PDF rotation
- **Tip**: Include shebang line (`#!/usr/bin/env python3`)
- **Benefits**: Token efficient, deterministic, may be executed without loading into context. Scripts may still need to be read by the assistant for patching or environment-specific adjustments.

## references/

Documentation loaded on demand to inform the assistant's process and thinking.

- **When to include**: For documentation the assistant should reference for specific scenarios
- **Examples**: API specs, database schemas, company policies, detailed workflow guides
- **Best practice**: For files >100 lines, include a table of contents. Avoid deeply nested references — keep one level deep from SKILL.md.
- **Avoid duplication**: Information lives in EITHER SKILL.md OR references, not both.

## assets/

Files used in the output, not loaded into context.

- **When to include**: Templates, boilerplate code, images, fonts
- **Examples**: `assets/logo.png`, `assets/slides.pptx`, `assets/frontend-template/`
- **Benefits**: Separates output resources from documentation. The assistant can use these files without loading them into context.

## Naming Conventions

- Skill name: kebab-case, lowercase letters + digits + hyphens only
- Directory name: matches skill name exactly
- Script files: snake_case, descriptive names (e.g., `rotate_pdf.py`)
- Reference files: kebab-case, descriptive names (e.g., `api-reference.md`)
