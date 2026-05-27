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

**Structure Rules**

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
- **Editing or reviewing an existing skill?** → Phase 2 Drafting
- **Just validating or packaging?** → Jump to Phase 3 or Phase 4
//register

### Phase 1: Pre-Creation Alignment
//?简化or加引到图
//总要test不写skill自己跑是不是也行，太简单or太复杂，合并gril 
//!带skill比不带还差 → skill可能过度约束，考虑精简----确立基线
// trigger scenarios, ...Proactively ask questions about edge cases, input/output formats, example files, success criteria, and dependencies. Wait to write test prompts until you've got this part ironed out.
Skip this step only when usage patterns are already clearly understood.

#### Step 1. Understand intent and extract workflow
   - Ask the user to clarify domain, use cases, and practical tasks/functionality, one question at a time.
   - If the current conversation already contains a workflow to capture (e.g., "turn this into a skill"), extract it
   - **If not**: Suggest that the user complete a real task in conversation first, then crystalize the workflow. 
   - **Output**: Write to `wip/workflow-extraction.md` with successful steps, failures/corrections, input/output formats, tools, and any project‑specific facts/doc/conventions, or constraints. 
   - Confirm your understanding with the user before proceeding.
   //记录流程，不要清理过程文件，最后再总结清理

#### Step 2. Search for similar skills and decide direction
   - Based on the confirmed understanding, search local repos and online platforms for matching skills. Follow `references/skillSearchList.md` for the full search strategy.
   - Read `ref-skills/_summary.md` and review the SKILL.md copies in `ref-skills/`.
   - **If similar skills exist**:
     → Present your recommendations to the user and clarify differences
     → Discuss one decision at a time to reach a shared understanding on how to extend or modify the reference skills, together with the workflow extraction.
     → Walk down each branch of the design tree, resolving dependencies step by step and filling the gaps.
   - **If no similar skills found, or the user chooses not to use them**:
     → Use the workflow extraction from Step 1 as input.
   - Confirm with the user then proceed to **Phase 2: Drafting**.

//Skip this phase only when usage patterns are already clearly understood.

//+claude plus：you can also run the skill description improver, which we have a whole separate script for, to optimize the triggering of the skill.


### Phase 2: Draft the Skill.md

Base on the outputs from Phase 1, set up `skill-name/`, draft `SKILL.md`and creat boundled resources.

Optionally, run `scripts/init_skill.py <name> --path <dir>` to generate a template with reusable example files. After initialization, customize or remove the generated SKILL.md and example files as needed.

No need to create README, CHANGELOG, INSTALLATION_GUIDE, or other auxiliary files.

Follow below guides. If updating an existing skill, skip directory creation and work directly on the existing files.

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


**Template with Recommended Sections**

```md
# Skill Name

## Overview 
[Purpose + Scope/Exclusion (+ Minimal working example)]

## Top Reminders
- [Core Principles/Critial Rules and Constraints, serving as entry quality gates. e.g. can include Alwyas, Must, Never items]
- Mindset Warning:
   [End this section with these real case excuses agents use to rationalize its way out of following the workflows]
   | Rationalization | Reality |
   |---|---|
   | "I know this workflow / task type." | Past experience ≠ current spec. Re-check. |
   | "I've handled an emergency" | You might be lost in the middle. Finish all steps |
   | "The main doc gave me the overview, so I don't need the ref." | Required refs contain critical steps not in the main doc. Read them. |


## Workflows and Output Formats (see details below)
[The heart of the skill, step-by-step processes]
[Output Template / Bullets / Example]


## Guardrails

### Critical Gotchas
| ID | Issue / Symptom | Fix |
|----|----------------|-----|
| G01 | (Example) | (How to avoid) |
| ...|...|...|

> After each run, agent may propose new gotchas. User approval required to update table or esclate severe ones to Top Reminder. Trival gotchas and long explanations go to `references/gotchas/`.

## Verification with Evidence
[After completing the skill's process, confirm and provide:]
| Check | Evidence |
|-------|----------|
| [ ] Exit criteria | [e.g., reviewed trigger list] |
| [ ] Format compliance | [e.g., paste output snippet] |
| ...|...|
[- Top Reminders should be checked.
 - Use scripts when necessary]

 ## Advanced features

[Link to separate files: See [...]]

```
**Workflows Detail Guide**

   - Start with a process overview – Use TL;DR, decision tree, or ASCII flowchart at decision points
   - Break operations into numbered, actionable phases or steps, include working examples where they help
   - Give the agent freedom when multiple approaches / variation are permitted — explain the goal
   - Consider pseudocode for complex conditional and algorithmic logic, etc. to improve precision and sequence consistency over plain text.
   - Add utility scripts for deterministic, code-repetitive and error-prone tasks (e.g., validation, formatting), scripts handle erros explicitly and reduce variability. 
   - Most skills have a mix. Calibrate each part independently
   - See references/workflows.md for workflow pattern examples (sequential, conditional, iteration)
   - Split long SKILL.md content into referenced files under Progressive Disclosure Structure Rules.

  
**Input and Output**: 
   - Use checklists for complex tasks to avoid skipping steps, especially when steps have dependencies or validation gates.
   - Use predefined templates for rigid output; Use bullet points to guide flexible output; Add quick examples if needed.
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
  
**Cross-Skill References**

Reference other skills by name:

```
Follow the `test-driven-development` skill for writing tests.
If the build breaks, use the `debugging-and-error-recovery` skill.
```

Don't duplicate content between skills — reference and link instead.

??----skill mgr

### Phase 3: Validate as you go

- Run `scripts/quick_validate.py <skill-dir>` after significant edits for static validation, fix any return error and discuss warnings with the user for quick act.

- Create only the resource types the workflow needs (scripts, references, assets). Test scripts by actually running them; delete unneeded files.


Iterate – fix any issues, re‑run the validation script, and re‑check manually until the skill is ready for use.

 ???  human
??? checklist?
- Start by writing a draft and then look at it with fresh eyes and improve it.


### Phase 4: Package a Skill
//skill git mgr
When the skill is complete, package it for distribution:

```bash
scripts/package_skill.py <path/to/skill-folder> [output-directory]
```

This automatically runs full validation (frontmatter, naming, structure, description quality) before packaging. If validation fails, fix errors and re-run. On success, creates a `<skill-name>.skill` file.


## Verification with Evidence

### Phase 5: Iterate ++++git一开始就要++register

After real usage, collect feedback and improve:

1. Use the skill on real tasks and note struggles or inefficiencies
2. Identify what to update in SKILL.md or bundled resources
3. Implement changes, re-validate (`quick_validate.py`), re-package if distributing
4. Test again

Common iteration triggers: missing trigger scenarios in description, overly long SKILL.md body that should be split to references, script bugs discovered in real use, or missing edge cases.

## Guardrails

### Critical Gotchas
| ID | Issue / Symptom | Fix |
|----|----------------|-----|
| G01 | ... | ... |


> After each run, agent may propose new gotchas. User approval required to update table or esclate severe ones to Top Reminder. Trival gotchas and long explanations go to `references/gotchas/`.



## Detailed Guides

Load these references when the corresponding scenario arises:

- **Scenario walkthroughs** — See [references/scenarios.md](references/scenarios.md) for end-to-end demonstrations (creating from scratch, updating existing, packaging only) with concrete examples. Load when stuck or learning by example.

