---
name: skill-name-in-kebab-case
description: Brief description of capability. Use when [specific triggers]. Maximum 1024 characters.
version: 1.0.0
# Optional Hermes-specific fields (for catalog discoverability):
# metadata:
#   hermes:
#     tags: [keyword, tags]
#     related_skills: [other-skill-name]
---

# Skill Name

## Overview

Purpose + Scope / Exclusion. Minimal working example.

The Overarching Process:
   → Read Overview and Critical Directives
   → Follow Workflows with Pre-Step Rationalization Bias Check
   → After run and before exit:
      1. Evolution
      2. Exit Verification

## Critical Directives

- Core principles / entry constraints serving as quality gates.
- Last point: Files Are Truth — Read, Don't Recall.
  The file on disk is the canonical source for rules and procedures; context and memory are stale shadows.

## Workflows and Output Formats

### Pre-Step Rationalization Bias Check (Mandatory — before every step)

1. **Re-read.** Files may change without notice — every operation guided by a file requires a fresh read.
2. **Follow references.** If a step says "see references/...", read every detail — no spot-checking.
3. **Check completion.** Review completed work and re-engage any missing steps — don't assume done.

[The heart of the skill: step-by-step processes, output templates, examples]

## Evolution

### Knowledge Classification

When new knowledge needs to be recorded, determine its type:

📚 **Reference knowledge** (diagnostics, architecture deep-dives, benchmarks, config comparisons, examples)
  → Create `references/<topic>.md` following conciseness and progressive disclosure rules
  → Always add a one-line link reference in the relevant SKILL.md section
  → **No approval needed** — no procedure change to SKILL.md

⚠️ **Gotcha / 😊 Success Pattern**
  → Record directly in the tables below (default).
  → When a table exceeds **5 rows**, archive older or less important entries to `references/evolution.md`.
  → **No approval needed** for any of these — they document experience, not procedure.

  Archive flow:
  ```
  evolution.md (full archive)  ←→  SKILL.md summary table (up to 5 key rows)
  ```

📝 **Procedure change** (modifying workflow steps, critical directives, commands that change behavior)
  → Propose to user → on approval: edit SKILL.md

### Trigger

Depends on the agent platform:

- **Platform supports editing skills mid-conversation** (e.g., Hermes has `skill_manage(action='patch')`)
  → Record immediately upon discovery
- **Platform does NOT support mid-conversation editing**
  → Check for new knowledge at the end of each run (Exit Verification stage) and record then

Procedure changes always need user approval regardless of platform.

### Critical Gotchas (Mandatory — seed at creation)

| ID | Issue / Symptom | Fix |
|----|----------------|-----|
| TBD | (Replace with the first gotcha discovered in actual use) | |

### Success Patterns (Mandatory — seed at creation)

| Date | Change | Context | Result |
|------|--------|---------|--------|
| TBD | (Replace with the first success pattern discovered in actual use) | | |

### Reference Index

Full index of reference files is maintained in `references/evolution.md`. Check there to find a specific reference file.

## Exit Verification

[Before exit, do overall verification: follow references/verification-gate.md to devise checks.]

| Check | Evidence |
|-------|----------|
| [ ] Exit criteria | [e.g., reviewed trigger list] |
