# Scenario Walkthroughs

> Load when you need end-to-end examples of using this skill — creating a new skill from scratch, updating an existing one, or packaging for distribution. Each scenario shows the complete flow with concrete commands and decisions.

## Scenario A: Creating a New Skill from Scratch

**Trigger**: User says "Build me a skill that processes podcast audio files"

### Flow

1. **Phase 1 — Understand intent and extract workflow (Step 1)**
   - Ask: "What operations should this skill support? Transcribing? Editing? Converting formats?"
   - Ask: "What would trigger this skill? Give me 2-3 example user requests."
   - Write findings to `.wip/workflow-extraction.md`
   - Confirm understanding with the user

2. **Phase 1 — Search for similar skills and decide direction (Step 2)**
   - Search for existing audio/podcast skills using `references/skillSearchList.md`
   - If similar skills found: present comparison, discuss differences, decide on approach
   - If none found or user opts out: proceed with workflow extraction as sole input

3. **Phase 2 — Set up directory structure and git**
   - Create the directory as shown in the Anatomy diagram
   - Ensure git tracking from the start (init if not already a repo)

4. **Phase 2.1 — Draft frontmatter**
   - Write `name: podcast-editor` and a description with "Use when" triggers
   - Follow the frontmatter rules: third-person, imperative, explicit triggers

5. **Phase 2.2 — Draft body and bundled resources**
   - Refer to Standard Sections (Recommended Pattern) for the body layout
   - Check `references/structure-examples.md` if a non-standard architecture fits better
   - Write the actual bundled resources:
     - Audio conversion script (deterministic, repeated task)
     - ffmpeg reference guide (too detailed for SKILL.md body)
     - Delete the `assets/` directory if not needed

6. **Phase 2.3 — Fresh eyes review** — Re-read the draft and improve before validating

7. **Phase 3 — Validate**
   Run `scripts/quick_validate.py podcast-editor/`, fix any errors, discuss suggestions with user.
   Test scripts by running them; complete the Verification checklist (Phase 3.2).

8. **Phase 4 — Package**
   Run `scripts/package_skill.py podcast-editor/`. Creates `podcast-editor.skill` on success.

9. **Phase 5 — Iterate** — After real usage, refine based on feedback

---

## Scenario B: Updating an Existing Skill

**Trigger**: User says "My PDF skill should also support splitting PDFs"

### Flow

1. **Skip Phase 1** — The skill already exists, use case is known
2. Read the existing SKILL.md and all bundled resources
3. **Phase 2 — Draft the update**:
   - Ensure git tracking (init if not already a repo)
   - Add the split-pdf script — write, test, and iterate
   - Update frontmatter description to include the new trigger
   - Update body to cover the new capability (Standard Sections as reference)
4. **Phase 3 — Validate**: Run `scripts/quick_validate.py pdf/`
5. **Phase 4 — Package and test**

---

## Scenario C: Validating and Packaging Only

**Trigger**: User says "Package my skill for distribution"

### Flow

1. **Skip to Phase 3** — No editing needed
2. **Phase 3 — Validate**: Run `scripts/quick_validate.py <skill-dir>`, fix any errors.
3. **Phase 4 — Package**: Run `scripts/package_skill.py <skill-dir>` (auto-validates as safety net).
4. Deliver the `.skill` file

---

## Scenario D: Reviewing Skill Quality

**Trigger**: User says "Review my skill for best practices"

### Flow

1. Read the skill's SKILL.md and bundled resources in full
2. **Check against the three Core Principles**:
   - **Concise is Key** — Challenge each section: "Would the agent get this wrong without it?" Cut if no.
   - **Progressive Disclosure** — Is body under 500 lines? Are bundled resources properly split? Any duplication?
   - **Mindset Warning** — Does the skill contain a rationalization table to preempt agent self-deception?
3. **Check Standard Sections coverage** — Do the sections (or equivalent headings) serve their intended purposes?
4. **Run structural validation**: `scripts/quick_validate.py <skill-dir>`
5. Report findings with specific, actionable recommendations — not vague opinions
