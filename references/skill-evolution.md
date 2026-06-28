## Reference Index

| File | Topic |
|------|-------|
| _(Add a row for each reference file created)_ | |

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
