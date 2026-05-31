# Design Examples

Load when: need end-to-end examples or help structuring a skill's body/workflow steps.

---

## Part 1: Scenario Walkthroughs

### Scenario A: Creating a New Skill from Scratch
**Trigger**: "Build me a skill that processes podcast audio files"

1. **Phase 1 — Understand intent (Step 1)**
   - Ask: "What operations? Transcribing? Editing? Converting?"
   - Ask: "What would trigger this skill? 2-3 example requests."
   - Write findings to `.wip/workflow-extraction.md`. Confirm with user.

2. **Phase 1 — Search and refine (Step 2)**
   - Search using `references/search-compare.md`
   - If similar skills found: present comparison, discuss, decide direction.
   - Ask: "Further refine using these results?" → refine or proceed.

3. **Phase 2 — Anatomy + Drafting**
   - Create directory structure (Anatomy diagram). Git init.
   - Draft frontmatter (name + description with "Use when" triggers).
   - Draft body per the Standard Sections template.
   - Check `## Part 2` below for alternative body structures.

4. **Phase 3 — Validate**: `scripts/quick_validate.py podcast-editor/`, fix errors, fill checklist.

5. **Phase 4 — Package**: `scripts/package_skill.py podcast-editor/`.

### Scenario B: Updating an Existing Skill
**Trigger**: "My PDF skill should also support splitting PDFs"

1. Read existing SKILL.md and all bundled resources.
2. **Phase 2 — Draft update**: git init if needed, add script, update frontmatter + body.
3. **Phase 3 — Validate**: `scripts/quick_validate.py pdf/`
4. **Phase 4 — Package**.

### Scenario C: Validating and Packaging Only
**Trigger**: "Package my skill for distribution"

1. **Phase 3 — Validate**: `scripts/quick_validate.py <skill-dir>`, fix errors.
2. **Phase 4 — Package**: `scripts/package_skill.py <skill-dir>`.
3. Deliver the `.skill` file.

### Scenario D: Reviewing Skill Quality
**Trigger**: "Review my skill for best practices"

1. Read the skill's SKILL.md and bundled resources in full.
2. **Check against the three Core Principles**:
   - **Concise is Key** — Challenge each section: "Would the agent get this wrong without it?" Cut if no.
   - **Progressive Disclosure** — Body ≤ 500 lines? Bundled resources properly split? No duplication?
   - **Files Are Truth — Read, Don't Recall** — Are workflow rules read from current files, not from context/memory?
3. **Check Standard Sections coverage** — Do sections (or equivalents) serve their purposes?
4. Run `scripts/quick_validate.py <skill-dir>`. Report findings with specific recommendations.

---

## Part 2: Structure Patterns

Two-level guide for organizing skill content:

### Body Architecture — Choosing the Overall Structure

Standard Sections (Overview / Critical Directives / Workflows / Exit Verification) are a recommended starting point, not a rigid template. Common alternatives:

**1. Workflow-Based** (sequential processes)
- Example: DOCX skill — "Workflow Decision Tree" → "Reading" → "Creating" → "Editing"
- Fits when: one primary task with ordered sub-steps

**2. Task-Based** (tool collections)
- Example: PDF skill — "Quick Start" → "Merge PDFs" → "Split PDFs" → "Extract Text"
- Fits when: several loosely-related capabilities

**3. Capabilities-Based** (integrated systems)
- Example: Product Management — "Core Capabilities" → numbered feature list
- Fits when: interrelated features, users chain several in one session

**4. Reference/Guidelines** (lookup resource)
- Example: Brand styling — flat topic list, no ordered workflow
- Fits when: consumed as reference, not process

Patterns can be combined.

### Step Design — Writing Workflow Steps

**Sequential Steps**: For complex tasks, break into ordered steps. Give the agent an overview early.

**Conditional Branching**: Guide the agent through decision points without forcing irrelevant reading.

**Iterative Optimization Loop**: Use pseudocode for quality-improvement cycles with precise logic.
