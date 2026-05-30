---
name: zao-skill
description: >
  Guide the complete lifecycle of agent skills — from design and drafting to review,
  packaging, and evolution through real usage. Use when the user wants to create a
  new skill, improve an existing skill, review skill quality, package a skill, or
  learn about skill design, progressive disclosure, or guardrails and evolution.
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

| Root Bias | Typical Rationalization | Reality Check |
|-----------|------------------------|----------------|
| **Memory reliance** | "I've seen this file before." ;"I've done similar tasks before." | Memory is unreliable. **Re-read the current state** before deciding. |
| **Closure seeking** | "I've handled that emergency / sub-task, so I'm done."| Don't assume completion. **Check if there are remaining steps** . |
| **Cognitive laziness** | "Checking this one field/trigger is enough to know it's fine.";"The main doc gave me the overview, ref is no need."  | Spot-check is not reliaable. Each verification is an investment, not a waste. **Do the full check**.  Required refs contain critical info not in the main doc. |

---

## Workflows and Output Formats

Jump to the phase that matches your need to start.

### Overview

```
Start → User Need?
   ├─ Create new skill              → Phase 1: Design
   ├─ Draft / update / edit skill   → Phase 2: Drafting
   ├─ Review / validate             → Phase 3: Validation
   └─ Package for release           → Phase 4: Packaging
```

Jump to the phase that matches your current need.

### Phase 1: Design

#### Step 1. Understand intent and extract workflow

- **If the conversation already contains a workflow** (e.g., "turn this into a skill") → Extract it to the output file and interview for anything unclear, one question at a time.

- **If not** → See `references/design-gate.md` Part 1 for the full interview and judgment protocol.

- **Output**: Write to `<skill-name>-wip/workflow-extraction.md`, covering triggers, successful steps, failures/corrections, input/output formats, tools, and any project‑specific facts/doc/conventions, or constraints.   Present for confirmation before proceeding.

#### Step 2. Search for similar skills and refine the design

**2.1 Ask**: "Search for existing similar skills (local repos / online platforms)?" 
- **If No** → Skip to Phase 2 with Step 1 output.

**2.2 If yes**→ Follow `references/skillSearchList.md` to execute search. 
- If nothing is found, inform the user and skip to Phase 2 with Step 1 output.

**2.3 Present the summary and Ask**, "Further refine the design using these results?" 
   - **If the user doesn't want to refine** → Proceed to Phase 2 with Step 1 output.
   - **Refine** → Follow `references/design-gate.md` Part 2 for the full refinement protocol. 
   After refinement, proceed to Phase 2 with outputs from Step 1 and 2.

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
   - description: Start with what the skill does, then include one or more clear "Use when" trigger conditions. Maximum 1024 characters. All "when to use" info goes here, not in the markdown instructions.

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

- Follow Core Principles. Be concise and use progressive disclosure. Every section must justify its inclusion — if removing it wouldn't change agent behavior, remove it
- Try to explain to the model why things are important in lieu of heavy-handed MUSTs in workflow section. 
- Use theory of mind and try to make the skill general and not super-narrow to specific examples.


**Standard Sections (Recommended Pattern)**

The frontmatter contract above is required. The section layout below is a recommended pattern, not a rigid template: equivalent headings are acceptable when they serve the same purpose clearly.

```md
# Skill Name

## Overview 
[Purpose + Scope/Exclusion (+ Minimal working example)]

## Top Reminders
- [Core Principles/Critical Rules/Entry Behaviour and Constraints, serving as entry quality gates. e.g. can include Always, Must, Never items]
- Mindset Warning://prevent step-skipping in long process
   [End this section with these real case excuses agents use to rationalize its way out of following the workflows]
   | Root Bias | Typical Rationalization | Reality Check |
   |-----------|------------------------|----------------|
   | **Memory reliance** | "I've seen this file before." ;"I've done similar tasks before." | Memory is unreliable. **Re-read the current state** before deciding. |
   | **Closure seeking** | "I've handled that emergency / sub-task, so I'm done."| Don't assume completion. **Check if there are remaining steps** . |
   | **Cognitive laziness** | "Checking this one field/trigger is enough to know it's fine.";"The main doc gave me the overview, ref is no need."  | Spot-check is not reliaable. Each verification is an investment, not a waste. **Do the full check**.  Required refs contain critical info not in the main doc. |


## Workflows and Output Formats (see Workflows Detail Guide below)
[The heart of the skill, step-by-step processes]
[Output Template / Bullets / Example]

## After Completing the Requested Workflow: Evolution Check

**Trigger**: Agent self-checks after each run: 
 did it produce a repeatable fix or a meaningful improvement?  
- If uneventful, skip. 
- If yes → follow `references/skill-evolution.md` to maintain following tables.

### Critical Gotchas
| ID | Issue / Symptom | Fix |
|----|----------------|-----|
| G01 | (Example) | (How to avoid) |
| ...|...|...|

### Success Patterns
| Date | Change | Trigger | Result |
|------|--------|---------|--------|
| -- | -- | -- | -- |
| -- | -- | -- | -- |
| -- | -- | -- | -- |



## Verification with Evidence (see Design Detail Guide below)
[After completing the skill's process, confirm and provide:]
| Check | Evidence |
|-------|----------|
| [ ] Exit criteria | [e.g., reviewed trigger list] |

## Advanced features

[Link to separate resources files: See [...]]

```
**Workflows Detail Guide**

   - Start with a process overview – Use TL;DR, decision tree, or concise ASCII flowchart at decision points
   - Break operations into numbered, actionable phases or steps, include working examples where they help
   - Match specificity to the task's fragility. Most skills have a mix to calibrate:
      - Give the agent freedom when multiple approaches / variation are permitted — explain the goal and logic to explore
      - Consider pseudocode for complex conditional and algorithmic logic, etc. to improve precision and sequence consistency over plain text
      - Add utility scripts for deterministic, code-repetitive and error-prone tasks (e.g., validation, formatting), scripts handle errors explicitly and reduce variability.
   - Split long SKILL.md content into referenced files under Progressive Disclosure Structure Rules.
   - See `references/structure-examples.md` for pattern examples

  
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


**How to Cross-Reference Another Skill**

Reference other skills by name:

```
Follow the `test-driven-development` skill for writing tests.
If the build breaks, use the `debugging-and-error-recovery` skill.
```

Don't duplicate content between skills — reference and link instead.

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
   → If new gotchas were discovered during validation, propose them for the Critical Gotchas table.
   → On user approval: exit Phase 3.


### Phase 4: Package a Skill


When jumping directly here (skipping Phase 3), package_skill.py auto-runs validation as a gate. In the normal flow, this re-validation is a harmless safety net.

```bash
scripts/package_skill.py <path/to/skill-folder> [output-directory]
```

Reports any FAIL items before packaging. On success, creates a `<skill-name>.skill` file.


## After Completing the Requested Workflow: Evolution Check

**Trigger**: Agent self-checks after each run: 
 did it produce a repeatable fix or a meaningful improvement?  
- If uneventful, skip. 
- If yes → follow `references/skill-evolution.md` to maintain following tables.

### Critical Gotchas
| ID | Issue / Symptom | Fix |
|----|----------------|-----|
| G01 | (Example) | (How to avoid) |
| ...|...|...|

### Success Patterns
| Date | Change | Trigger | Result |
|------|--------|---------|--------|
| -- | -- | -- | -- |
| -- | -- | -- | -- |
| -- | -- | -- | -- |



## Scenario Examples

Load these references when the corresponding scenario arises:

- **Scenario walkthroughs** — See [references/scenarios.md](references/scenarios.md) for end-to-end demonstrations (creating from scratch, updating existing, packaging only) with concrete examples. Load when stuck or learning by example.

