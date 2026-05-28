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
  Covers full lifecycle: alignment, drafting, validation, packaging, and iteration.
---

# Zao Skill 

## Overview (Purpose/Quick Start)

Skills are modular packages that provide specialized knowledge, workflows, and tools to AI agents.
This skill guides the creation, review, and maintenance of effective skills.

---

## Core Principles

### 1. Concise is Key

**Default assumption: the agent is already smart.** Only add context it doesn't have. The context window is a public good. Every token in your skill competes for the agent’s attention with conversation history, system context, and other active skills. Focus on what the agent wouldn’t know without your skill.

**Prefer concise examples over verbose explanations.** Challenge each piece in your skill: "Does the agent really need this explanation?" or “Would the agent get this wrong without this instruction?” If the answer is no, cut it. 

### 2. Progressive Disclosure

**Anatomy of a Skill**
```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description required)
│   └── Markdown instructions body
└── Bundled Resources (optional)
    ├── scripts/    - Executable code for deterministic/repetitive tasks
    ├── references/ - Docs loaded into context as needed
    └── assets/     - Files used in output (templates, icons, fonts)
```

Skills use a three-level loading system and should be structured to take advantage of this progressive disclosure mechanism:

 1. Metadata (name + description) - Always in context (~100 words)
 2. SKILL.md body - In context whenever skill triggers (<500 lines ideal)
 3. Bundled resources - As needed (unlimited, scripts can execute without loading)

**Progressive Rules**

- Keep SKILL.md body under 500 lines; if approaching this limit, split into Bundled Resources and link them from SKILL.md with clear "when to read" guidance
- Keep file references one level deep from SKILL.md and for large reference files (>300 lines), include a table of contents
- Avoid duplication: Each reference MUST add genuinely new value — never repeat what SKILL.md already says.
- The agent reads only the relevant reference file. So keep reference files focused.

**Example: Domain organization**

When a skill supports multiple domains/frameworks, organize by variant:
```
cloud-deploy/
├── SKILL.md (workflow + selection)
└── references/
    ├── aws.md
    ├── gcp.md
    └── azure.md
```

### 3. Mindset Warning

| Rationalization | Reality |
|---|---|
| "I know this workflow / task type." | Past experience ≠ current spec. Re-check. |
| "I've handled an emergency" | You might be lost in the middle. Finish all steps |
| "The main doc gave me the overview, so I don't need the ref." | Required refs contain critical steps not in the main doc. Read them. |


---

## Workflows and Output Formats

**Choose your entry point based on user's need**:

- **Creating a new skill?** → Phase 1 Alignment
- **Drafting or editing an existing skill?** → Phase 2 Drafting
- **Just reviewing or validating** → Phase 3 Validation
- **Just packaging** → Phase 4 Packaging
//?Testing
//register

### Phase 1: Pre-Creation Alignment
//?简化or加引到图
//总要test不写skill自己跑是不是也行，太简单or太复杂，合并gril 
//!带skill比不带还差 → skill可能过度约束，考虑精简----确立基线
//centralized registry?

#### Step 1. Understand intent and extract workflow
   - Ask the user to clarify domain, use cases, and practical tasks/functionality, one question at a time.
   - If the current conversation already contains a workflow to capture (e.g., "turn this into a skill"), extract it
   - **If not**: Suggest that the user complete a real task in conversation first, then crystalize the workflow. 
   - **Output**: Write to `<skill-name>-wip/workflow-extraction.md` with successful steps, failures/corrections, input/output formats, tools, and any project‑specific facts/doc/conventions, or constraints. 
   - Confirm your understanding with the user before proceeding.
   //记录流程，不要清理过程文件，最后再总结清理

#### Step 2. Search for similar skills and decide direction
   - Based on the confirmed understanding, search local repos and online platforms for high-matching skills. Follow `references/skillSearchList.md` for the full search strategy.
   - Read `_summary.md` and review the SKILL.md copies in `<skill-name>-wip/ref-skills/`.
      - **If similar skills exist**:
      → Present your recommendations to the user and clarify differences
      → Discuss one decision at a time to reach a shared understanding on how to extend or modify the reference skills, together with the workflow extraction.
      → Walk down each branch of the design tree, resolving dependencies step by step and filling the gaps.
      - **If no similar skills found, or the user chooses not to use them**:
      → Use the workflow extraction from Step 1 as input.
   - Confirm with the user then proceed to **Phase 2: Drafting**.

---

### Phase 2: Draft the Skill.md

**For a new skill** — create the directory structure as shown in the Anatomy diagram above.

**For an existing skill** — work directly on the existing files.

**Either way** — ensure git tracking from the start.

#### **2.1 Draft Frontmatter (Required)**

```md
---
name: skill-name-in-kebab-case
description: Brief description of capability. Use when [specific triggers].
---
```
   **Frontmatter Rules**:
   - name: skill identifier.
   - description: Start with what the skill does in third person, then include one or more clear "Use when" trigger conditions. Include both what and when. Maximum 1024 characters. All "when to use" info goes here, not in the markdown instructions.

   **Purpose**:
   - Under progressive disclosure, the description is **the only thing the agent sees** when deciding which skill to load. 
   - It carries the entire burden of skill triggering.

   **Writing Patterns**
   - Use imperative phrasing
   - Explicitly list contexts where the skill applies
   - Focus on user intent, not implementation steps

   **Example**:
   - Bad example: "How to build a simple fast dashboard to display internal Anthropic data."
   - Good example: "How to build a simple fast dashboard to display internal Anthropic data. Make sure to use this skill whenever the user mentions dashboards, data visualization, internal metrics, or wants to display any kind of company data, even if they don't explicitly ask for a 'dashboard.'"


#### **2.2 Draft Body Sections and Bundled Resources**

**Writing Rules**

- Prefer using the imperative and concise form. (Core Principles 1)
- Progressive disclosure. Main SKILL.md is the entry point. (Core Principles 2)
- Valuable and non-duplicate. Every section must justify its inclusion. If removing it wouldn't change agent behavior, remove it.
- Try to explain to the model why things are important in lieu of heavy-handed musty MUSTs. 
- Use theory of mind and try to make the skill general and not super-narrow to specific examples.


**Standard Sections (Recommended Pattern)**

The frontmatter contract above is required. The section layout below is a recommended pattern, not a rigid template: equivalent headings are acceptable when they serve the same purpose clearly.

```md
# Skill Name

## Overview 
[Purpose + Scope/Exclusion (+ Minimal working example)]

## Top Reminders
- [Core Principles/Critial Rules/Entry Behaviour and Constraints, serving as entry quality gates. e.g. can include Alwyas, Must, Never items]
- Mindset Warning://prevent step-skipping in long process
   [End this section with these real case excuses agents use to rationalize its way out of following the workflows]
   | Rationalization | Reality |
   |---|---|
   | "I know this workflow / task type." | Past experience ≠ current spec. Re-check. |
   | "I've handled an emergency" | You might be lost in the middle. Finish all steps |
   | "The main doc gave me the overview, so I don't need the ref." | Required refs contain critical steps not in the main doc. Read them. |


## Workflows and Output Formats (see Workflows Detail Guide below)
[The heart of the skill, step-by-step processes]
[Output Template / Bullets / Example]


## Verification with Evidence (see design guide below)
[After completing the skill's process, confirm and provide:]
| Check | Evidence |
|-------|----------|
| [ ] Exit criteria | [e.g., reviewed trigger list] |


## Guardrails

[### Anti-Patterns / Constraints(Optional)]

### Critical Gotchas
| ID | Issue / Symptom | Fix |
|----|----------------|-----|
| G01 | (Example) | (How to avoid) |
| ...|...|...|

### Evolution
| Date | Change | Trigger | Result |
|------|--------|---------|--------|
| -- | -- | -- | -- |
| -- | -- | -- | -- |
| -- | -- | -- | -- |

> After each run → new gotchas. After each successful iteration → new evolution entry.
> Keep 3 of each here. Archive older entries to `<skill-name>-wip/skill-log.md`.
> User approval required to update tables or escalate severe gotchas to Top Reminder.


## Advanced features

[Link to separate resources files: See [...]]

```
**Workflows Detail Guide**

   - Start with a process overview – Use TL;DR, decision tree, or ASCII flowchart at decision points
   - Break operations into numbered, actionable phases or steps, include working examples where they help
   - Match specificity to the task's fragility. Most skills have a mix to calibrate:
      - Give the agent freedom when multiple approaches / variation are permitted — explain the goal and logic to explore
      - Consider pseudocode for complex conditional and algorithmic logic, etc. to improve precision and sequence consistency over plain text
      - Add utility scripts for deterministic, code-repetitive and error-prone tasks (e.g., validation, formatting), scripts handle erros explicitly and reduce variability. 
   - Split long SKILL.md content into referenced files under Progressive Disclosure Structure Rules.
   - See `references/structure-design.md` for pattern examples

  
**Input and Output**: 
   - Use checklists for complex tasks to avoid skipping steps, especially when steps have dependencies or validation gates.
   - Use predefined templates for rigid output; Use bullet points to guide flexible output; Add quick examples if needed.
   - Can be used as quality gates between phases/steps
   - Consider user confirmation checkpoints when necessary.
   
   ```md
   ## Quick Example 1: Report structure
   ALWAYS use this exact template:
   # [Title]
   ## Executive summary
   ## Key findings
   ## Recommendations
   ```

   ```md
   ## Quick Example 2: Commit message format
   **Example 1:**
   Input: Added user authentication with JWT tokens
   Output: feat(auth): implement JWT-based authentication
   ```

**Verification Design Guide**

Can be merged into Workflows and Input/Output or as independent section.

Generally, Divide checks into two layers:
- **Script** — deterministic, regex‑able: line counts, syntax, reference existence, table format
- **Checklist** — requires reading content: conciseness, duplication, guide compliance. Each item is a yes/no question, one dimension each

Design rules:
- Only check against rules stated in the skill's text. Don't invent standards
- Evidence column stays empty — the agent fills it after inspecting its own output
- Every finding cites the specific line number. No vague claims

Loop structure:
   Run script → fix FAILs → fill Evidence → fix gaps → re‑run script
   Stop when: zero FAILs + all Evidence filled + user approves
   Save each round to <skill-name>-wip/validation‑round‑N.md

**Guardrails Detail Guide**

Critical Gotchas and Evolution are paired: one records failures, the other records wins. Together they form the iteration safety net.

- Commit baseline before any change. One change per iteration
- After each real usage → new gotchas. After each successful change → new evolution entry
- Test the change on the next real task: improved → keep. Worse → `git revert`, log as gotcha
- Keep 3 entries in each table. Archive older to `<skill-name>-wip/skill-log.md`
  
**Cross-Skill References**

Reference other skills by name:

```
Follow the `test-driven-development` skill for writing tests.
If the build breaks, use the `debugging-and-error-recovery` skill.
```

Don't duplicate content between skills — reference and link instead.

//??----skill mgr

#### **2.3 When the SKILL.md and its resources have been drafted in complete, re-read once with fresh eyes for improvements. Then proceed to Phase 3 Validation

---

### Phase 3: Validate as you go

**Scope-lock** :
- Polish how the skill works, don't change what it does. No new capabilities, no new dependencies.
- Every finding must cite the specific line number. No vague claims.
- Don't apply changes without user confirmation.

**Repeat until user approves:**

   #### 3.1 Static Validation
   Run `scripts/quick_validate.py <skill-dir>`. Report every FAIL item with proposed fix. Apply only after user confirmation.

   > Script checks are signals to review, not mandates — some checks don't apply to every architecture. When in doubt, ask the user.

   #### 3.2 Verification with Evidence
   Work through the checklist. Fill Evidence for each item — quote specific content, not opinions. Report gaps and proposed fixes; apply only after user confirmation.

   | Check | Evidence |
   |-------|----------|
   | [ ] Instructions are concise and actionable? | |
   | [ ] Every section justifies its inclusion? | |
   | [ ] No duplicated content between body and references? | |
   | [ ] Standard section elements all present? | |
   | [ ] Workflow detail guides followed? | |
   | [ ] Input / output formats properly defined? | |
   | [ ] Re-read with fresh eyes? | |

   Save the filled checklist and script output to `<skill-name>-wip/validation-round-N.md`.

   If script fixes were applied, go back to 3.1.
   If checklist gaps were fixed, re-check only those items.

   #### 3.3 Approval Gate
   When 3.1 has zero FAILs and 3.2 Evidence is all filled:
   → Ask user whether fine with this phase. Show the latest <skill-name>-wip/validation-round-N.md path.
   → On user approval: exit Phase 3.


### Phase 4: Package a Skill


When jumping directly here (skipping Phase 3), package_skill.py auto-runs validation as a gate. In the normal flow, this re-validation is a harmless safety net.

```bash
scripts/package_skill.py <path/to/skill-folder> [output-directory]
```

Reports any FAIL items before packaging. On success, creates a `<skill-name>.skill` file.


### Phase 5: Iterate 

After each real usage, accumulate experience — one change at a time:

1. Use the skill on a real task. Note what worked and what didn't
2. Commit the current state as baseline before changing anything
3. Identify one improvement. Don't batch multiple changes
4. Implement the change, re-validate (`quick_validate.py`), re-package if distributing
5. Use the skill on the next real task. Compare with baseline:
   - Improved → keep. Record in Evolution table
   - Worse → `git revert`. Log as gotcha. Try a different approach
6. Record: new gotchas → Critical Gotchas table; successful changes → Evolution table.
   Full history in `<skill-name>-wip/skill-log.md`.

Common iteration triggers: missing trigger scenarios in description, overly long SKILL.md body that should be split to references, script bugs discovered in real use, or missing edge cases.


## Guardrails

### Critical Gotchas
| ID | Issue / Symptom | Fix |
|----|----------------|-----|
| G01 | Template references `references/gotchas/` but directory doesn't exist → script reports "all valid" FAIL | Create the directory or remove the reference |

### Evolution
| Date | Change | Trigger | Result |
|------|--------|---------|--------|
| -- | -- | -- | -- |
| -- | -- | -- | -- |
| -- | -- | -- | -- |

> After each run → new gotchas. After each successful iteration → new evolution entry.
> Keep 3 of each here. Archive older entries to `<skill-name>-wip/skill-log.md`.
> User approval required to update tables or escalate severe gotchas to Top Reminder.


## Scenario Examples

Load these references when the corresponding scenario arises:

- **Scenario walkthroughs** — See [references/scenarios.md](references/scenarios.md) for end-to-end demonstrations (creating from scratch, updating existing, packaging only) with concrete examples. Load when stuck or learning by example.

