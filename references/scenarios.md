# Scenario Walkthroughs

> Load when you need end-to-end examples of using this skill — creating a new skill, updating an existing one, or packaging for distribution. Each scenario shows the complete flow with concrete commands and decisions.

## Scenario A: Creating a New Skill from Scratch

**Trigger**: User says "Build me a skill that processes podcast audio files"

### Flow

1. **Understand the use case** (Step 1)
   - Ask: "What operations should this skill support? Transcribing? Editing? Converting formats?"
   - Ask: "What would trigger this skill? Give me 2-3 example user requests."

2. **Plan resources** (Step 2)
   - Identify: Need a script for audio conversion (repeated task)
   - Identify: Need reference docs for ffmpeg command flags (too detailed for SKILL.md)
   - Identify: No assets needed

3. **Initialize** (Step 3)
   ```bash
   scripts/init_skill.py podcast-editor --path skills/
   ```

4. **Edit** (Step 4)
   - Write `scripts/convert_audio.py` — test it
   - Write `references/ffmpeg-guide.md`
   - Delete `assets/` (not needed)
   - Fill in SKILL.md frontmatter and body
   - Run `scripts/quick_validate.py podcast-editor/` after each major edit

5. **Package** (Step 5)
   ```bash
   scripts/package_skill.py skills/podcast-editor
   ```

6. **Iterate** (Step 6) — After real usage, refine based on feedback

## Scenario B: Updating an Existing Skill

**Trigger**: User says "My PDF skill should also support splitting PDFs"

### Flow

1. **Jump to Step 4** — The skill already exists, no need to re-understand or plan
2. Read the existing SKILL.md and bundled resources
3. Add the new capability:
   - Add `scripts/split_pdf.py`
   - Update `SKILL.md` frontmatter description to mention the new trigger
   - Update SKILL.md body to include the new workflow
4. Run `scripts/quick_validate.py <skill-dir>` to validate
5. Package and test

## Scenario C: Validating and Packaging Only

**Trigger**: User says "Package my skill for distribution"

### Flow

1. **Jump to Step 5** — No editing needed
2. Run `scripts/package_skill.py <skill-dir>`
3. If validation fails, fix the reported issues
4. Deliver the `.skill` file

## Scenario D: Reviewing Skill Quality

**Trigger**: User says "Review my skill for best practices"

### Flow

1. **Review Core Principles in SKILL.md** — Evaluate skill against the four design principles (Concise, Appropriate Degrees of Freedom, Progressive Disclosure, Comprehensive Description)
2. Read the skill's SKILL.md and references
3. Check against the four core principles:
   - Is it concise? (challenge each section)
   - Are degrees of freedom appropriate? (text vs scripts)
   - Does it use progressive disclosure? (over 500 lines? proper references? no duplication?)
   - Is the description comprehensive? (all triggers listed?)
4. Run `scripts/quick_validate.py <skill-dir>` for structural issues
5. Report findings with specific recommendations
