# Skill Evolution — Full Archive

## How to Use This File

This file stores the **complete archive** of gotchas and success patterns for this skill.
The most critical current entries are summarized in SKILL.md's tables — this file holds everything else.

### Trigger

- **If the agent platform supports editing skills mid-conversation** (e.g., Hermes with `skill_manage`)
  → Record new discoveries immediately, before context is lost
- **Otherwise**
  → Check at the end of each run (Exit Verification) and record any new insights

### Record Flow

```
New insight discovered
  → Add to SKILL.md's Critical Gotchas or Success Patterns table (default location)
  → When the table exceeds N rows (recommended: 5), move older entries here as narrative records
  → If the insight is a reference document (diagnosis, comparison, architecture analysis),
    create references/<topic>.md instead
```

### What to Record

- **Gotcha** — a failure with a repeatable fix. Record the symptom, root cause, and the fix.
- **Success Pattern** — a workflow or approach that proved reliably better. Record the change, the context, and the result.
- **Neither** — trivial changes (typos, one-line updates). No recording needed.

### Version Conventions

When updating this skill, update the `version` field in SKILL.md frontmatter:
- Major restructure → bump major (1.x → 2.x)
- New content (new section, new reference) → bump minor (1.2 → 1.3)
- Minor fix → version unchanged

---

## Gotchas Archive

### 2026-05-30 — [G01] Memory Reliance
**Issue:** Wrote Success Patterns from stale context / injected text instead of the current file on disk.
**Root cause:** Context freezes at load time; the agent assumed memory was current without re-reading the file.
**Fix:** Always re-read the target file before any edit operation. The file on disk is the source of truth.

### 2026-05-30 — [G02] Closure Seeking
**Issue:** After completing the description + skillSearchList fix, assumed the full workflow was done. Skipped the evolution-approval step.
**Root cause:** Premature completion bias — one sub-task success triggered false "done" signal.
**Fix:** Review the full step checklist after each sub-task. Don't assume completion until every step is verified.

### 2026-05-30 — [G03] Cognitive Laziness
**Issue:** Skipped reading `skill-evolution.md` reference (the current file). Also wrote to the template's table instead of zao-skill's own Critical Gotchas / Success Patterns.
**Root cause:** Two tables with the same name (template vs zao-skill's own) caused confusion. Reference files skipped due to lazy reading.
**Fix:** Follow every "see references/X" instruction. Scan for naming ambiguity when two tables with the same label exist in different scopes.

---

## Success Patterns Archive

### YYYY-MM-DD — (example) Increased Response Accuracy
By adjusting the temperature parameter from 0.7 to 0.3 for factual queries, accuracy improved from 82% to 94%. The change was validated across 3 different skill types. Lower temperature may not work well for creative tasks — keep that in mind.

### YYYY-MM-DD — (example) Profile-based Compression Strategy
Created separate profiles for serious vs casual work, one with compression disabled and one with default settings. This preserves full context for critical conversations while still saving tokens on casual chat. No loss of information on important sessions.
