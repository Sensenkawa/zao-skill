# zao-skill · 造技能

**The Meta-Skill Framework — AI creating skills for AI.**

A design-to-maintenance lifecycle framework for building production-grade AI agent skills. zao-skill treats AI behavior drift, unreliable execution, and unmaintainable evolution as first-class design problems — not afterthoughts.

[![GitHub release](https://img.shields.io/github/v/release/Sensenkawa/zao-skill?include_prereleases&label=version&style=flat-square)](https://github.com/Sensenkawa/zao-skill/releases)
[![License](https://img.shields.io/github/license/Sensenkawa/zao-skill?style=flat-square)](LICENSE.txt)

---

## Core Design

### 1. Three-Layer Anti-Drift Architecture

| Layer | Mechanism | Role |
|-------|-----------|------|
| **Principle** | Files Are Truth | Declarative: set the rule |
| **Execution** | Pre-Step Rationalization Bias Check | Actionable: must pass before every operation |
| **Feedback** | Gotchas G01–G03 (real failure cases) | Archival: replay error patterns |

### 2. Knowledge-Driven Evolution

Skills accumulate three types of knowledge:

| Type | Where it goes | Approval needed? |
|------|---------------|:----------------:|
| Reference knowledge | `references/<topic>.md` + link in SKILL.md | No |
| Gotcha / Success Pattern | SKILL.md summary table → archive to `references/evolution.md` when >5 rows | No |
| Procedure change | Edit SKILL.md directly | **Yes** — propose to user |

**Key decision**: knowledge is recorded directly in the summary table first. No judgment of "is this important enough?" — only "is the table full?" When it exceeds 5 rows, older entries flow to the archive.

### 3. Dual-Lane Validation

- **Static check** — `quick_validate.py`: syntax, format, structure
- **Interactive check** — Human-in-the-loop evidence checklist

---

## Workflow Overview

```
Pre-Step Rationalization Bias Check (before every phase)
                │
                ▼
        ┌──────────────┐
        │  User Need?  │
        └──────┬───────┘
               │
    ┌──────────┼──────────┐
    ▼          ▼          ▼
Phase 1:  Phase 2:   Phase 3:
Design    Drafting   Validation
    │          │          │
    └──────────┴──────────┘
               │
               ▼
        Phase 4: Packaging (optional)
               │
               ▼
           Evolution
      (continuous, no approval for
       knowledge; procedure changes
       require user approval)
```

---

## Quick Start

```bash
# Load the skill
"Use zao-skill to create a new skill"
```

Every execution follows this outer process:
```
→ Read Overview and Critical Directives
→ Follow Workflows with Pre-Step Rationalization Bias Check
→ After run and before exit:
    1. Meta Evolution Check (zao-skill's own scope-ruled evolution)
    2. Exit Verification
```

Phase flow:
```
User Need?
  ├─ Phase 1: Design     — interview → search → run-first → LOOP confirm
  ├─ Phase 2: Drafting   — frontmatter + standard sections + Evolution [Must have]
  ├─ Phase 3: Validation — quick_validate.py + evidence checklist + Evolution setup check
  └─ Phase 4: Packaging  — package_skill.py (platform-dependent, optional)
All paths → Evolution in Usage
```

---

## Meta-Skill Note

zao-skill eats its own dog food:
- ✅ Uses its own design protocol
- ✅ Passes its own validation
- ✅ Records its own gotchas (G01–G03 from real failures)
- ✅ Maintains its own success patterns
- ✅ Version-controlled with semantic tags (three-segment `major.minor.patch`)
- ✅ Reference files follow naming conventions
- ✅ Evolution section follows the [Must have] requirements it prescribes

---

## License

MIT
