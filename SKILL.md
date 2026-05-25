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

### 2. Anatomy of a Skill

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description required)
│   └── Markdown instructions
└── Bundled Resources (optional)
    ├── scripts/    - Executable code for deterministic/repetitive tasks
    ├── references/ - Docs loaded into context as needed
    └── assets/     - Files used in output (templates, icons, fonts)
```

Only include what the agent needs to do the job. Do NOT create README, CHANGELOG, INSTALLATION_GUIDE, or other auxiliary files.

### 3. Progressive Disclosure
Skills use a three-level loading system and should be structured to take advantage of this:

 1. Metadata (name + description) - Always in context (~100 words)
 2. SKILL.md body - In context whenever skill triggers (<500 lines ideal)
 3. Bundled resources - As needed (unlimited, scripts can execute without loading)

#### Guidelines

- Keep SKILL.md under 500 lines; if approaching this limit, split into Bundled Resources and link them from SKILL.md with clear "when to read" guidance
- Keep file references one level deep from SKILL.md and for large reference files (>300 lines), include a table of contents
- Avoid duplication: Each reference must add genuinely new value — never repeat what SKILL.md already says.
- The agent reads only the relevant reference file. So keep reference files focused.

#### Example: Domain organization
When a skill supports multiple domains/frameworks, organize by variant:
```
cloud-deploy/
├── SKILL.md (workflow + selection)
└── references/
    ├── aws.md
    ├── gcp.md
    └── azure.md
```
---

## Workflows and Output Formats

Choose your entry point based on user's need:

- **Creating a new skill?** → Phase 1 Alignment
- **Updating or reviewing an existing skill?** → Phase 2 Drafting
- **Just validating or packaging?** → Jump to Validate & Package

### Phase 1: Pre-Creation Alignment

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

Base on the outputs from Phase 1, create `skill-name/` with `SKILL.md`and draft the SKILL.md following the template and rules below. Optionally, run `scripts/init_skill.py <name> --path <dir>` to generate a template with example files.
//都可以删掉？----更新skill git manager
   - SKILL.md with concise instructions
   - Additional reference files if content exceeds 500 lines
   - Utility scripts if deterministic operations needed

#### Part 1. YAML Frontmatter (Required)

```md
---
name: skill-name-in-kebab-case
description: Brief description of capability. Use when [specific triggers].
---
# Skill Name
[Markdown instructions]
```

   **Rules**:
   - name: skill identifier.
   - description: Start with what the skill does in third person, then include one or more clear "Use when" trigger conditions. Include both what and when. Maximum 1024 characters. All "when to use" info goes here, not in the markdown instructions.

   **Purpose**:
   - Under progressive disclosure, the description is **the only thing the agent sees** when deciding which skill to load. 
   - It carries the entire burden of skill triggering.

   **Patterns**
   - Use imperative phrasing
   - Explicitly list contexts where the skill applies
   - Focus on user intent, not implementation steps

   **Example**:
   - Bad example: "How to build a simple fast dashboard to display internal Anthropic data."
   - Good example: "How to build a simple fast dashboard to display internal Anthropic data. Make sure to use this skill whenever the user mentions dashboards, data visualization, internal metrics, or wants to display any kind of company data, even if they don't explicitly ask for a 'dashboard.'"


#### Part 2. Markdown Instruction Modules (Recommanded)

```md
# Skill Name

## Overview 
[Purpose + Scope/Exclusion (+ Minimal working example)]

## Top Reminders
- [Core Principles/Critial Rules, serving as entry quality gates. eg, can include Alwyas, Must, Never items]
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

```
**Workflows Detail Guide**

   - An process overview on top, use concise flowcharts (ASCII) / decision tree / TL;DR where decision points exist
   - Break operations into numbered and actionable phases or steps, include working examples where they help
   - Give the agent freedom when multiple approaches are valid and the task tolerates variation — explaining why and goal can be helpful
   - Consider using pseudocode for complex condition logics, algorithm-like steps, etc. to increases precision and sequence consistency beyond text-based instructions.
   - Add utility scripts when the operation is deterministic and error-prone (e.g., validation, formatting), the same code would be generated repeatedly, or errors need explicit handling. 
   - Most skills have a mix. Calibrate each part independently
   - 缺少用户确认检查点 → 在关键决策处插入
   · 清晰定义边界：明确能做什么、不能做什么，以及失败时的降级策略或人工介入条件。

**Input and Output**: 
   - Use checklists for complex tasks to avoid skipping steps, especially when steps have dependencies or validation gates
   - 

输出模板vs输出要点;补充格式、路径、示例
?pattern, , contraints(anti-patterns)
?
?common edge cases?
output 2 formats: template, bullets, examples--Examples pattern- It's useful to include examples

constraints-skill manager 衔接

5. 确保 references 文件有价值
检查references/output-patterns.md和的内容是否：
• 是 SKILL.md 的补充，而不是重复
• 提供了 SKILL.md 中没有的新信息
• 如果内容重复，应该合并到 SKILL.md 或删除

   - **Body**: Imperative form. Keep under 500 lines. Only operational instructions — teaching material goes in references.


2. **Write bundled resources** — Create scripts, references, and assets as the workflow demands. Test scripts by actually running them. Delete unneeded files. Not every skill needs all three resource types — only create what the workflow requires.
//-----pocock，2.0提及了吗？其他两个呢。前面还是后面


3. 

4. **Validate as you go**: Run `scripts/quick_validate.py <skill-dir>` after significant edits for fast feedback. See references/output-patterns.md and references/workflows.md for design patterns (output formats, workflow structures).

If updating an existing skill, skip directory creation and work directly on the existing files.

### Phase 3: Validate & Package

When the skill is complete, package it for distribution:

```bash
scripts/package_skill.py <path/to/skill-folder> [output-directory]
```

This automatically runs full validation (frontmatter, naming, structure, description quality) before packaging. If validation fails, fix errors and re-run. On success, creates a `<skill-name>.skill` file.

### Phase 4: Iterate

After real usage, collect feedback and improve:

1. Use the skill on real tasks and note struggles or inefficiencies
2. Identify what to update in SKILL.md or bundled resources
3. Implement changes, re-validate (`quick_validate.py`), re-package if distributing
4. Test again

Common iteration triggers: missing trigger scenarios in description, overly long SKILL.md body that should be split to references, script bugs discovered in real use, or missing edge cases.

## Detailed Guides

Load these references when the corresponding scenario arises:

- **Scenario walkthroughs** — See [references/scenarios.md](references/scenarios.md) for end-to-end demonstrations (creating from scratch, updating existing, packaging only) with concrete examples. Load when stuck or learning by example.
- **Design patterns** — See [references/output-patterns.md](references/output-patterns.md) for output templates and [references/workflows.md](references/workflows.md) for workflow patterns (sequential, conditional, entry-point). Load when choosing output formats or process structures.
