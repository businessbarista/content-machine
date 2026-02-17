# Content Type: Playbook

## Overview

- **Command flag:** `--playbook [YouTube URL]`
- **Description:** A tactical, step-by-step guide extracted from an expert's video interview — structured as a standalone playbook readers can execute immediately.
- **Length:** 2,500-4,000 words
- **Platform:** Web / newsletter

---

## Pipeline

**Pipeline: custom**

This content type uses a custom 5-step pipeline (P1-P5) rather than the standard content machine pipeline.

```
P1: Transcript   → Fetch and validate the source material
P2: Extraction    → Structure raw material into playbook elements
P3: Draft         → Write the full playbook using the format spec
P4: Council       → Review via the Playbook Council (6 reviewers)
P5: Revision      → Iterate to 9/10 score
```

---

### STEP P1: TRANSCRIPT (Fetch the Source Material)

**Goal:** Get the full YouTube transcript as raw text.

**Output location:** `projects/[project-name]/1_transcript/raw_transcript.md`

#### P1.1: Create Project Folder

When the user provides a YouTube URL, create the project folder:

```
projects/[expert-name]-[topic-slug]/
├── 1_transcript/
├── 2_extraction/
└── 3_playbook/
```

Name the project folder based on the video title or content (e.g., `drew-bredvick-sales-agent`, `ash-tilawat-eval-framework`).

#### P1.2: Fetch Transcript

Run the transcript fetcher:

```bash
bash scripts/fetch-transcript.sh "[YouTube URL]"
```

Save the output to `1_transcript/raw_transcript.md` with metadata:

```markdown
# Transcript — [Video Title]

**Source:** [YouTube URL]
**Expert:** [Name if identifiable from video title]
**Date Fetched:** [date]

---

[FULL TRANSCRIPT TEXT]
```

#### P1.3: Transcript Quality Check

Before proceeding, verify:
- Transcript is in English
- Transcript is substantive (>1000 words — enough for a meaningful playbook)
- Transcript contains teachable/tactical content (not just casual chat)

**If transcript fetch fails or is unavailable:**
1. Inform the user: "Couldn't fetch the transcript automatically."
2. Offer alternatives:
   - "Can you paste the transcript directly?"
   - "Try a different video from the same expert"
   - "I can try fetching via WebFetch as a fallback"

Once transcript is saved, move to Step P2.

---

### STEP P2: EXTRACTION (Structure the Raw Material)

**Goal:** Extract structured elements from the transcript to populate the playbook template.

**Output location:** `projects/[project-name]/2_extraction/extraction.md`

#### P2.1: Expert Profile Extraction

Extract from the transcript (and video title/description if available):

```markdown
## THE HUMAN

**Name:** [Expert's full name]
**Title/Role:** [Current title, company]
**Background:** [2-3 sentence bio based on what they share in the video]
**Key Credential:** [Specific achievement that establishes authority — numbers, scale, outcomes]
**Personality Quote:** [A quote from the transcript that captures how they think]
**Social Link:** [If mentioned in video, otherwise flag as missing]
```

**CRITICAL:** If any fields are unclear from the transcript, present what you found and ASK THE USER to fill gaps.

Wait for user confirmation before proceeding.

#### P2.2: Framework Extraction (The Loop)

Identify the expert's core methodology/framework:

```markdown
## THE LOOP

**Framework Name:** [If they name it, use their name. If not, create a descriptive one.]
**Core Sequence:** [The steps/phases in order — brief, one line each]
**Key Principle:** [The underlying philosophy that makes this framework work]
**Contrast:** [How this differs from how most people approach this problem]
**Conditions:** [When this works / when it doesn't]
```

#### P2.3: Steps Extraction

For each distinct step/phase in the expert's process:

```markdown
## STEPS

### Step 1: [Action-Oriented Title]
**Core Idea:** [1-2 sentences]
**Key Quote:** "[Direct quote from transcript]"
**Tactical Details:** [Specific tools, numbers, processes mentioned]
**Stories/Examples:** [Specific anecdotes the expert shared about this step]
**Pro Tip Material:** [An insider insight or non-obvious tip]
**Checkpoint Material:** [What the reader should be able to do after this step]

### Step 2: [...]
[...continue for all steps identified]
```

**Extraction rules:**
- Preserve the expert's exact language for quotes
- Capture specific numbers, tool names, company names, timeframes
- Note where the expert gave a concrete example vs. spoke abstractly
- Identify 5-7 steps (merge if too granular, split if too broad)

#### P2.4: Quotes & Stories

```markdown
## QUOTABLE MOMENTS

> "[Quote 1]" — [context]
> "[Quote 2]" — [context]
[...aim for 8-12 strong quotes]

## STORIES & ANECDOTES

### Story 1: [Title]
[Full story as told by expert — preserve their words]

### Story 2: [Title]
[...]
```

#### P2.5: FAQ Material

```markdown
## FAQ MATERIAL

[Questions that arose naturally in the video]
[Common objections the expert addressed]
[Practical "but what about..." concerns they covered]
```

#### P2.6: User Confirmation

Present the full extraction to the user and wait for confirmation before proceeding to drafting.

---

### STEP P3: DRAFT (Write the Playbook)

**Goal:** Produce a complete playbook draft.

**Output location:** `projects/[project-name]/3_playbook/playbook_draft.md`

#### P3.1: Read the Format Spec + Lessons

**CRITICAL:** Before drafting, read:
1. The **Format Specification** section of this content type spec (below)
2. `content-lessons.md` (Playbook Lessons section) — Accumulated lessons from past playbook feedback

**If a lesson in `content-lessons.md` conflicts with this spec, the lesson takes priority.**

Apply:
- The exact document structure (Opening Block → Numbered Steps → Closing Block)
- Voice and tone rules (second person, conversational-authoritative, expert words preserved)
- Required elements in every step (Pro Tip, Checkpoint, expert blockquote)
- Anti-patterns to avoid (no corporate speak, no generic examples, no paraphrased-to-blandness quotes)
- Playbook-specific lessons from past projects

#### P3.2: Draft the Opening Block

Write in this order:

**1. Title**
Format: "[How to / The X-Step / Build...]: [Specific Outcome]"
- Must promise a specific, desirable result
- Under 15 words

**2. The Human**
- Expert profile as narrative prose (2-3 paragraphs)
- Specific credential with numbers
- Personality quote
- Social link

**3. The Loop**
- Framework overview with core sequence
- Expert quote
- When it works / when it doesn't

**4. Use Cases**
- 3-5 specific persona descriptions
- Who should skip this

#### P3.3: Draft the Numbered Steps

For each step extracted in P2:

1. **Number + punchy action title:** `## 01. [Title]`
2. **Italicized tagline:** `*[One-line tone setter]*`
3. **Narrative body** (2-4 paragraphs mixing editorial voice with expert's actual words)
4. **Code blocks / templates / schemas** where the content is technical
5. **`Pro Tip:`** — one per step, always present
6. **`Checkpoint:`** — one per step, always present
7. **At least one blockquoted expert quote** per step

**CRITICAL DRAFTING RULES:**
- **Preserve the expert's actual words** wherever possible — the transcript IS your raw material
- Use **second person** ("you") throughout
- Include **specific numbers, tool names, timeframes** — never vague
- Every step must be **actionable**, not just conceptual
- Match the playbook tone: confident, slightly contrarian, no corporate speak
- **Do NOT use your personal social voice** — playbooks are editorial/authoritative, not casual lowercase

#### P3.4: Draft the Closing Block

**1. FAQs:** 4-6 questions with direct, no-hedge answers
**2. The Takeaway:** 2-3 paragraphs — the bigger "so what" / contrarian implication
**3. CTA:** (customize for your company/brand — see CTA template in the format specification below)

#### P3.5: Self-Review Checklist

Before sending to the Playbook Council, verify:

| Check | Requirement |
|-------|-------------|
| Structure | The Human → The Loop → Use Cases → Steps → FAQs → Takeaway → CTA |
| Expert Voice | Direct quotes in every section, personality preserved |
| Actionability | Each step has a concrete action the reader can take |
| Pro Tips | One per step, all present |
| Checkpoints | One per step, all present |
| Specificity | Numbers, tool names, timeframes throughout |
| Tone | Second person, conversational-authoritative, no corporate speak |
| Length | 2,500-4,000 words total |
| Anti-slop | No "delve," "landscape," "game-changer," "leverage," "robust," "seamless" |

---

### STEP P4: PLAYBOOK COUNCIL

Uses the modified Playbook Council (see **Council Adaptations** below).

**Output location:** `projects/[project-name]/3_playbook/council_review.md`

---

### STEP P5: REVISION LOOP (Iterate to 9/10)

**Goal:** Iteratively improve the playbook until the Playbook Council scores it 9/10 or higher.

**Output location:** `projects/[project-name]/3_playbook/FINAL_playbook.md`

Loop: Council Review → Score < 9? → Revise → Re-Review → Repeat until ≥ 9/10 or max 3 cycles.

**CRITICAL:** Maintain the playbook voice from the format specification above. Do NOT drift toward your personal social voice.

#### Final Output

When approved, save to `3_playbook/FINAL_playbook.md`:

```markdown
# [Playbook Title]

**Status:** Approved (9/10)
**Expert:** [Name], [Title]
**Source:** [YouTube URL]

---

[FULL FINAL PLAYBOOK]

---

*Generated via The Content Machine — Playbook Pipeline*
```

#### P5.5: Learn from This Playbook (Optional)

After saving, offer to learn from the revision history. If yes: run `--learn` on this project.

---

## Format Specification

This section is the definitive format reference for playbooks. Read this before drafting any playbook.

---

### Document Structure

Every playbook follows this exact structure:

```
┌────────────────────────────────────────────┐
│  OPENING BLOCK: "The Strategy"             │
│    → The Human (expert profile)            │
│    → The Loop (framework overview)         │
│    → Use Cases (who this is for)           │
├────────────────────────────────────────────┤
│  BODY: Numbered Steps (01–06)              │
│    → Each step: title, tagline, narrative, │
│      expert quotes, pro tip, checkpoint    │
├────────────────────────────────────────────┤
│  CLOSING BLOCK                             │
│    → FAQs (4-6 questions)                  │
│    → The Takeaway (the bigger "so what")   │
│    → CTA                                   │
└────────────────────────────────────────────┘
```

---

### Opening Block: "The Strategy"

#### The Human

The expert introduction. Written as narrative prose, not a bullet list.

**Required elements:**
- Expert's full name
- Current title and company
- 2-3 sentence background establishing credibility (specific numbers, accomplishments)
- A personality-revealing quote — something that captures how they think, not just what they did
- Link to follow them (X/Twitter or LinkedIn)

**Format example:**
```markdown
### The Human

**[Name]** is the [title] at [company]. [Background sentence with specific credential — numbers, scale, outcomes]. [Second sentence adding personality or origin story].

**Key Perspective:** "[A quote that reveals their philosophy or contrarian angle]"

[Follow them on X](https://x.com/handle)
```

**Tone:** Authoritative but human. The reader should think "this person has done the thing, I should listen."

---

#### The Loop

The framework distilled to its core sequence — the "spine" of the playbook.

**Required elements:**
- The methodology in 3-6 steps/phases (brief, one line each)
- 2-3 sentences explaining the underlying principle
- How this differs from the conventional approach
- A blockquoted expert quote with attribution
- When this works / when it doesn't (conditions)

**Format example:**
```markdown
### The Loop

The framework [Name] used is: **[Step 1] → [Step 2] → [Step 3] → [Step 4]**

- [Step 1 one-liner]
- [Step 2 one-liner]
- [Step 3 one-liner]
- [Step 4 one-liner]

[2-3 sentences on the underlying principle and what makes this approach different from the default.]

> "[Expert quote about the philosophy]"
> — **[Name], [Title]**
```

---

#### Use Cases

Who this playbook is for — and who it's NOT for.

**Required elements:**
- 3-5 specific persona descriptions (role + situation + pain point)
- Clear disqualification criteria (who should skip this)
- Written in second person

**Tone:** Direct, specific. Personas should feel like real people the reader might recognize as themselves.

---

### Body: Numbered Steps

Each step follows an identical internal structure. Typically 5-7 steps per playbook.

#### Step Header

```markdown
## 0X. [Action-Oriented Title]
```

- Always two-digit numbering (01, 02, 03...)
- Title is imperative/action-oriented: "Shadow + Watch", "Pull Historical Data", "Build Your Golden Set"
- Short — 2-5 words

#### Italicized Tagline

```markdown
*[One line that sets the tone for this section.]*
```

- Appears immediately after the header
- Sets emotional tone, not information
- Can be punchy, funny, metaphorical, or blunt
- Examples: *"Pull up a chair and a pen."* / *"The boring part that everything else depends on."*

#### Narrative Body

2-4 paragraphs mixing editorial voice with the expert's actual words.

**Rules:**
- Second person ("you") throughout
- Weave expert quotes directly into the narrative (not just blockquoted)
- Include specific numbers, tool names, timeframes
- Code blocks, YAML schemas, or templates where the content is technical
- Every step must be actionable — no purely conceptual sections

**Pattern:**
```
[Opening context: what this step is and why it matters]
[The expert's approach: what they actually did, in their words]
[Tactical details: specific tools, processes, numbers]
[Code/template block if applicable]
[Common pitfall or nuance]
```

#### Pro Tip

```markdown
**Pro Tip:** [Tactical insider advice the reader wouldn't think of on their own.]
```

- **One per step. Always present. Never skip.**
- Should be genuinely useful — not generic advice
- Often comes from the expert's direct experience
- Specific > general

#### Checkpoint

```markdown
**Checkpoint:** [What the reader should be able to do/say after completing this step.]
```

- **One per step. Always present. Never skip.**
- Phrased as a capability the reader now has
- Should be verifiable — the reader can check if they've actually done it
- Examples: "You have 30+ test cases with explicit constraints documented." / "Your agent has at least 3 tools it can use to take action in the world."

#### Expert Quotes (Blockquoted)

```markdown
> "[Direct quote from the expert]"
>
> **— [Name]**
```

- At least one blockquoted expert quote per step
- Preserve the expert's actual language, verbal tics, personality
- Place at moments of emphasis or transition
- Attribution format: bold name, optionally title

---

### Closing Block

#### FAQs

```markdown
## FAQs

### [Question in natural language?]

[2-4 sentence direct answer. No hedging.]

### [Question 2?]

[Answer.]
```

- 4-6 questions
- Questions should be things a reader would actually ask
- Cover: prerequisites, common objections, tool/cost questions, team dynamics
- Answers are direct — no "it depends" without then giving the real answer

#### The Takeaway

```markdown
## The Takeaway

[2-3 paragraphs synthesizing the bigger "so what."]
```

- Zoom out from the tactical to the strategic
- Slightly contrarian or provocative conclusion
- What this means for the reader's career, business, or industry
- Optional: bulleted checklist of questions for self-evaluation
- End with a line that sticks

#### CTA

Customize for your company/brand:

```markdown
## [Your CTA Headline]

[Your company] helps [audience] [value prop].

If you're ready to [connect to playbook topic], [we can help / CTA].

[**Get started →**]([your-url])
```

- 2-3 sentences max
- Connects to the playbook topic
- Single link

---

### Voice & Tone Rules

#### DO:
1. **Second person throughout** — "you," "your"
2. **Conversational but authoritative** — like a senior colleague walking you through something, not a textbook
3. **Expert's words are sacred** — preserve their actual language, verbal tics, specific terminology
4. **Confident and slightly contrarian** — take positions, don't hedge
5. **Specific over abstract** — numbers, tool names, timeframes, code examples
6. **Dry wit over jokes** — humor is allowed but never forced
7. **Editorial "we" sparingly** — "we're going to walk through" for transitions only
8. **Short paragraphs** — 2-4 sentences max, lots of whitespace
9. **Bold for emphasis** — key terms, key phrases, key names

#### DON'T:
1. **No corporate speak** — ban "leverage," "robust," "seamless," "comprehensive," "synergy," "landscape," "delve"
2. **No generic openings** — never start with "In today's fast-paced world..." or "As AI continues to evolve..."
3. **No generic examples** — every example should be specific to the expert's experience
4. **No purely conceptual steps** — every step must have a concrete action
5. **No paraphrasing quotes into blandness** — if the expert said "I'm not kidding," keep "I'm not kidding"
6. **No skipping Pro Tips or Checkpoints** — they are mandatory structural elements
7. **No CTA longer than 3 sentences**
8. **No uniform sentence rhythm** — vary short punchy sentences with longer explanatory ones
9. **No personal social voice** — playbooks are editorial/authoritative, not casual lowercase

---

### Formatting Reference

#### Length
- Total: 2,500-4,000 words
- Opening Block: 400-600 words
- Each Step: 300-500 words
- FAQs: 300-500 words
- Takeaway + CTA: 200-300 words

#### Markdown Elements Used
- `##` for major sections (The Human, The Loop, Steps, FAQs, Takeaway)
- `###` for subsections within steps
- `**bold**` for emphasis and key terms
- `*italic*` for taglines only
- `> blockquote` for expert quotes
- ` ``` code blocks ``` ` for code, YAML, templates, prompts
- `- bullet lists` for enumerations
- `| tables |` for comparison/reference data
- `---` horizontal rules between major sections

#### Structural Checklist

Before publishing, verify every playbook has:

| Element | Required | Location |
|---------|----------|----------|
| Expert name + credential | Yes | The Human |
| Expert personality quote | Yes | The Human |
| Social link | Yes | The Human |
| Framework overview | Yes | The Loop |
| Expert blockquote | Yes | The Loop |
| 3-5 persona descriptions | Yes | Use Cases |
| Numbered steps (01-07) | Yes | Body |
| Italicized tagline per step | Yes | Each step header |
| Pro Tip per step | Yes | Each step |
| Checkpoint per step | Yes | Each step |
| Expert blockquote per step | Yes | Each step |
| 4-6 FAQs | Yes | FAQs |
| Contrarian takeaway | Yes | The Takeaway |
| CTA with link | Yes | CTA |

---

## Council Adaptations

The Playbook Council is a modified version of the Writer's Council, tuned specifically for playbook review. It consists of 6 reviewers, each evaluating the playbook through a distinct lens.

### The Playbook Council Members

| Reviewer | Playbook Lens | Key Question |
|----------|--------------|--------------|
| **Morgan Housel** | Depth & Insight | "Is the underlying principle timeless, or just trendy?" |
| **Tim Urban** | Clarity & Structure | "Can a beginner follow this without getting lost?" |
| **Shaan Puri** | Hook & Opening | "Would someone click this and read past the intro?" |
| **Greg Isenberg** | Tactical Completeness | "Can someone actually DO this after reading?" |
| **David Perell** | Narrative Craft | "Does this tell a story, or is it just instructions?" |
| **Slop Detector** | Expert Fidelity | "Does this sound like the expert, or like an AI summary?" |

---

### 1. MORGAN HOUSEL (Depth & Underlying Insight)

**Reviews for:** Is there a deeper principle beneath the tactical steps? Will this framework matter in 5 years, or is it tied to a specific tool that'll be obsolete?

**Output:**
- Timeless Principle: [What's the enduring insight beneath the tactics?]
- Depth Check: [Are any sections surface-level?]
- Missing "Why": [Where does the playbook explain WHAT but not WHY?]
- Depth Rating: /10

### 2. TIM URBAN (Clarity & Beginner Accessibility)

**Reviews for:** Can someone who's never done this follow the steps? Are there knowledge gaps? Is the progression logical?

**Output:**
- Clarity Path: [Can you follow Step 1 → 2 → 3 without confusion?]
- Jargon Alert: [Terms used without explanation]
- Concept Gap: [Where does it jump from simple to complex too fast?]
- "Aha" Moment: [Is there a moment of delightful understanding?]
- Clarity Rating: /10

### 3. SHAAN PURI (Title, Hook & Opening)

**Reviews for:** Is the title click-worthy? Does the opening (The Human + The Loop) make you want to keep reading?

**Output:**
- Title Test: [Would you click this? Yes/No + why]
- Opening Energy: [Does The Human section hook you?]
- Promise Check: [Is the outcome specific enough?]
- 3 Alternative Titles: [options]
- Hook Rating: /10

### 4. GREG ISENBERG (Tactical Completeness & Actionability)

**Reviews for:** Can someone actually execute this? Are there missing prerequisites? Is every step specific enough?

**Output:**
- Execution Test: [Could someone follow this and produce a result?]
- Missing Step: [What's not covered that a reader would need?]
- Vague Alert: [Which steps are too abstract?]
- Pro Tip Quality: [Are the tips genuinely insider knowledge?]
- Steal Test: [What section would someone screenshot?]
- Actionability Rating: /10

### 5. DAVID PERELL (Narrative Craft & Expert Story)

**Reviews for:** Is this a compelling story wrapped around instructions? Does the expert come alive as a character?

**Output:**
- Expert as Character: [Does the expert feel real and interesting?]
- Story Arc: [Is there narrative momentum across the playbook?]
- POP Score: Personal __/10 | Observational __/10 | Playful __/10
- Memorable Line: [What's the one line people will quote?]
- Narrative Rating: /10

### 6. SLOP DETECTOR (Expert Fidelity & Authenticity)

**Reviews for:** Does this preserve the expert's actual voice? Or has it been smoothed into generic AI prose?

**Red flags for playbooks:**
- Expert quotes that all sound the same (homogenized)
- Steps that could apply to any topic (too generic)
- Missing the expert's specific terminology, verbal tics, or personality
- Uniform sentence rhythm across all sections
- "In this section, we'll explore..." type transitions
- Any of: "delve," "landscape," "game-changer," "leverage," "robust," "seamless"

**Output:**
- Expert Voice Score: /10
- Red Flag Phrases Found: [list any]
- Generic Alert: [Steps that feel template-y rather than specific]
- Lines That Sound Like the Expert: [2-3 lines that work]
- Priority Fidelity Fixes: [exact text + suggested fix]

---

### Final Synthesis

**Consensus Points:** [Where 2+ reviewers agreed]

**Priority Fixes (Ranked):**
1. [Most important — source reviewer]
2. [Second — source reviewer]
3. [Third — source reviewer]

**Overall Score:** /10

**One-Line Verdict:** [The single most important thing this playbook needs]

---

## Revision Notes

Playbook-specific tips for the revision loop (P5).

### Voice Drift Prevention

The most common failure mode in playbook revisions is **voice drift** — the playbook starts in the editorial/authoritative tone but gradually slides toward either generic AI prose or your personal social voice. During each revision pass:

- Re-read the Voice & Tone Rules in the format specification above before revising
- Check that the expert's actual words are still present and unsmoothed
- Verify sentence rhythm varies across sections — if everything reads the same cadence, rewrite
- Confirm no banned words have crept in ("delve," "landscape," "robust," etc.)

### Council Score Interpretation

- **9-10/10:** Ship it. Minor polish only.
- **7-8/10:** Structural bones are good, but 2-3 sections need rework. Typical first-pass score.
- **5-6/10:** Fundamental issues — missing expert voice, steps too generic, or structure off. Expect a significant rewrite.
- **Below 5:** Re-extract from transcript. The draft missed the core material.

### Common Revision Patterns

1. **"Too generic" feedback (Greg/Slop Detector):** Go back to the extraction. Find the specific numbers, tool names, and anecdotes you left on the table. The transcript almost always has more specificity than the draft uses.

2. **"Expert doesn't feel real" feedback (David/Slop Detector):** You've paraphrased too aggressively. Pull more direct quotes from the extraction. Let the expert's verbal tics and personality show through.

3. **"Missing the why" feedback (Morgan):** Add a paragraph to the relevant step explaining the underlying principle — why this works, not just what to do. Often the expert explained this in the interview but it didn't make it into the draft.

4. **"Confusing progression" feedback (Tim):** Steps may need reordering, or there's a prerequisite buried in Step 4 that should be in Step 1. Map the dependency chain and restructure.

5. **"Wouldn't click" feedback (Shaan):** The title is too generic or The Human section is a LinkedIn bio instead of an editorial on-ramp. Rewrite the opening with a specific, outcome-driven hook.

### Lessons Integration

Always check `content-lessons.md` (Playbook Lessons section) before revising. Accumulated lessons from past playbook feedback take priority over general rules when they conflict. Key recurring lessons include:

- Lead with credential, then the result (The Human section)
- The Human section is an editorial on-ramp, not a LinkedIn bio
- Use numbered lists for sequential frameworks, not bullets
- Sentence case for bold action words, not Title Case
- Don't editorialize on top of strong data — trust the proof

---

*This content type spec is self-contained. It defines the full playbook pipeline, format specification, council review process, and revision guidance. Reference `content-lessons.md` (Playbook Lessons section) for the latest accumulated lessons.*
