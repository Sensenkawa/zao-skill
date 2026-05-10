---
name: zao-skill
description: >-
  Guide for creating effective skills that extend AI agent capabilities.
  Use when users request to:
  (1) Create a new skill from scratch,
  (2) Update or improve an existing skill,
  (3) Review or validate skill quality against best practices,
  (4) Package a skill for distribution,
  (5) Learn skill design principles or structure conventions.
  Covers full lifecycle: initialization, resource planning, SKILL.md authoring,
  validation, and packaging.
license: Complete terms in LICENSE.txt
---

# Zao Skill

Skills are modular packages that provide specialized knowledge, workflows, and tools to AI agents.
This skill guides the creation, review, and maintenance of effective skills.

## Core Principles

1. **Concise is Key** — The context window is shared. Default assumption: the assistant is already smart. Only add context it doesn't have. Challenge each piece: "Does the assistant really need this explanation?"

2. **Set Appropriate Degrees of Freedom** — Match specificity to task fragility: high freedom (text instructions) for flexible tasks, medium (pseudocode/parameterized scripts) for preferred patterns, low freedom (specific scripts) for fragile or error-prone operations.

3. **Progressive Disclosure** — Three-level loading: metadata (always) → SKILL.md body (when triggered, keep under 500 lines) → bundled resources (as needed). Split detailed content into reference files when approaching the limit, always reference them from SKILL.md with clear "when to read" guidance.

4. **Self-Consistency** — The rules this skill teaches must be followed by this skill itself. Every principle, every structural requirement, every validation rule applies here first.

## Skill Structure

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter: name + description (required), optional: license, metadata, compatibility
│   └── Markdown body: operational instructions, kept lean
├── scripts/          - Executable code for deterministic or repeated tasks
├── references/       - Documentation loaded on demand for specific scenarios
└── assets/           - Files used in output (templates, fonts, etc.), not loaded into context
```

Only include what the agent needs to do the job. Do NOT create README, CHANGELOG, INSTALLATION_GUIDE, or other auxiliary files.

### Scripts Reference

| Script | When to Call | Purpose |
|--------|-------------|---------|
| `scripts/init_skill.py <name> --path <dir>` | Step 3: creating a new skill from scratch | Generates template with SKILL.md, example directories, and resource files |
| `scripts/quick_validate.py <skill-dir>` | Step 4: during editing, any time after changes | Fast check of frontmatter format, required fields, naming conventions, and description quality |
| `scripts/package_skill.py <skill-dir> [output-dir]` | Step 5: when ready to distribute | Full validation + creates distributable .skill file (zip archive) |

## Skill Creation Process

Choose your entry point based on what you need:

- **Creating a new skill?** → Start at Step 1
- **Updating or reviewing an existing skill?** → Jump to Step 4
- **Just validating or packaging?** → Jump to Step 5

### Step 1: Understand with Concrete Examples

Understand how the skill will be used through concrete examples. Ask the user focused questions about desired functionality, trigger scenarios, and expected inputs/outputs. Don't overwhelm — ask the most important questions first, follow up as needed.

Conclude when there is a clear sense of the functionality the skill should support.

Skip this step only when usage patterns are already clearly understood.

### Step 2: Plan Reusable Resources

Analyze each concrete example to identify reusable resources:

- **scripts/**: Code that would be rewritten repeatedly or needs deterministic reliability
- **references/**: Documentation the assistant should load for specific scenarios (schemas, APIs, policies)
- **assets/**: Files used in output rather than loaded into context (templates, images, fonts)

Create a concrete list of what each example needs. Not every skill needs all three types of resources.

### Step 3: Initialize

For new skills, run the init script to generate a template:

```bash
scripts/init_skill.py <skill-name> --path <output-directory>
```

This creates the directory structure, a SKILL.md template with TODO placeholders, and example files in scripts/, references/, and assets/.

After initialization, customize or delete the generated files as needed.

Skip this step if working with an existing skill.

### Step 4: Edit the Skill

Work in this order:

1. **Implement reusable resources first** — scripts, references, assets identified in Step 2. Test scripts by actually running them. Delete unneeded example files.

2. **Write SKILL.md**:
   - **Frontmatter**: `name` in kebab-case, `description` with BOTH what the skill does AND specific trigger scenarios (numbered list). All "when to use" info goes in description — not in body. Optional fields (`license`, `metadata`, `compatibility`) are rarely needed; only include them with clear purpose.
   - **Body**: Imperative form. Keep under 500 lines. Only operational instructions — teaching material goes in references.

3. **Validate as you go**: Run `scripts/quick_validate.py <skill-dir>` after significant edits for fast feedback. See references/output-patterns.md and references/workflows.md for design patterns (output formats, workflow structures).

### Step 5: Package

When the skill is complete, package it for distribution:

```bash
scripts/package_skill.py <path/to/skill-folder> [output-directory]
```

This automatically runs full validation (frontmatter, naming, structure, description quality) before packaging. If validation fails, fix errors and re-run. On success, creates a `<skill-name>.skill` file.

### Step 6: Iterate

After real usage, collect feedback and improve:

1. Use the skill on real tasks and note struggles or inefficiencies
2. Identify what to update in SKILL.md or bundled resources
3. Implement changes, re-validate (`quick_validate.py`), re-package if distributing
4. Test again

Common iteration triggers: missing trigger scenarios in description, overly long SKILL.md body that should be split to references, script bugs discovered in real use, or missing edge cases.

## Detailed Guides

Load these references when the corresponding scenario arises:

- **Design principles in depth** — See [references/principles.md](references/principles.md) for detailed explanations, progressive disclosure patterns, and anti-patterns. Load when designing a new skill or reviewing one against best practices.
- **Skill anatomy details** — See [references/anatomy.md](references/anatomy.md) for complete structure specifications of SKILL.md, scripts/, references/, and assets/. Load when unsure about structural rules.
- **Scenario walkthroughs** — See [references/scenarios.md](references/scenarios.md) for end-to-end demonstrations (creating from scratch, updating existing, packaging only) with concrete examples. Load when stuck or learning by example.
- **Design patterns** — See [references/output-patterns.md](references/output-patterns.md) for output templates and [references/workflows.md](references/workflows.md) for workflow patterns (sequential, conditional, entry-point). Load when choosing output formats or process structures.
