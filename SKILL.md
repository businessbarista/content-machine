---
name: content-machine
description: A complete content creation system. Interview Panel extracts your stories → Raw production file → Refinement with your writing style → Writer's Council editing → Revision loop until 9/10. Includes project organization and style guide.
---

# The Content Machine

A complete system for creating publish-ready content from your ideas.

```
┌─────────────────────────────────────────────────────────────────────┐
│                        THE CONTENT MACHINE                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  STEP 1: INPUT          → Interview panel helps find your topic     │
│            ↓                                                        │
│  STEP 2: INTERVIEW      → Panel extracts stories, insights, data    │
│            ↓                                                        │
│  STEP 3: PRODUCTION     → Interview → raw .md file (source of truth)│
│            ↓                                                        │
│  STEP 4: REFINEMENT     → Select content types, draft with style    │
│            ↓                                                        │
│  STEP 5: EDITING        → Writer's Council reviews and scores       │
│            ↓                                                        │
│  STEP 6: REVISION LOOP  → Iterate until 9/10                        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## System Structure

```
/content-machine/
├── SKILL.md              ← You are here (the process)
├── style-guide.md        ← Your writing voice
├── projects/
│   └── [project-name]/
│       ├── 1_input/      ← Topic selection
│       ├── 2_interview/  ← Interview transcript
│       ├── 3_production/ ← Raw .md file (source of truth)
│       ├── 4_refinement/ ← Platform drafts
│       ├── 5_editing/    ← Council review
│       └── 6_final/      ← Approved versions
└── archive/              ← Old/completed projects
```

---

## Quick Commands

**Full Pipeline (Steps 1-6):**
```
/content-machine --full [topic]
/content-machine --full (no topic - panel helps you find one)
```

**New Project:**
```
/content-machine --new [project-name]
```

**Start from Interview (Steps 1-4):**
```
/content-machine --interview [topic]
/content-machine --interview
```

**Council Review Only (Steps 5-6):**
```
/content-machine [paste your content]
```

**Revision Loop Only (Step 6):**
```
/content-machine --revise [paste your content]
```

**Single Reviewer:**
```
/content-machine --reviewer morgan [paste your content]
/content-machine --reviewer shaan [paste your content]
/content-machine --reviewer slop [paste your content]
```

---

## Creating a New Project

When starting a new piece of content, create a project folder:

```
/content-machine --new [project-name]
```

This creates:
```
projects/[project-name]/
├── 1_input/
├── 2_interview/
├── 3_production/
├── 4_refinement/
├── 5_editing/
└── 6_final/
```

All files for this content piece live in this folder, organized by step.

---

## The Teams

### The Interview Panel (Steps 1-2)

| Interviewer | Style | Known For |
|-------------|-------|-----------|
| **Tim Ferriss** | Tactical deconstruction | "What does the first 60 minutes look like?" |
| **Joe Rogan** | Follow the curiosity | "That's insane. Tell me more." |
| **Larry King** | Short, direct questions | "Why?" "How did that feel?" |
| **Howard Stern** | Disarmingly personal | Gets what you normally wouldn't say |
| **Michael Barbaro** | Narrative clarity | "Help me understand..." |
| **Barbara Walters** | Emotional depth | Finds the human truth |

### The Writer's Council (Steps 5-6)

| Writer | Superpower | Key Question |
|--------|-----------|--------------|
| **Morgan Housel** | Timelessness & Story | "Will this matter in 10 years?" |
| **Tim Urban** | Clarity & Delight | "Is this confusing anywhere?" |
| **Shaan Puri** | Hooks & Virality | "Would I stop scrolling?" |
| **Greg Isenberg** | Actionability | "What can someone steal?" |
| **David Perell** | Internet Writing Craft | "Is this POP?" |
| **Slop Detector** | AI Authenticity | "Could a machine have written this?" |

---

# STEP 1: INPUT (Topic Discovery)

**Goal:** Help the user identify a compelling topic to write about.

**Output location:** `projects/[project-name]/1_input/topic_selection.md`

If the user already has a topic, skip to Step 2.

If the user doesn't have a topic, the Interview Panel **collectively** suggests 5-6 compelling options based on:

- The user's background and unique experiences
- What would make compelling content
- Topics with emotional depth and universal resonance
- Contrarian or unexplored angles
- Stories only they can tell

**Output format:**
```
Here are 6 topics the panel thinks you should consider:

1. [Topic] — [One-line angle/hook]
2. [Topic] — [One-line angle/hook]
3. [Topic] — [One-line angle/hook]
4. [Topic] — [One-line angle/hook]
5. [Topic] — [One-line angle/hook]
6. [Topic] — [One-line angle/hook]

Which one resonates? Or tell us a different direction.
```

Once the user picks a topic → Move to Step 2.

---

# STEP 2: INTERVIEW (Extract the Raw Material)

**Goal:** Extract stories, insights, examples, and data through a conversational interview.

**Output location:** `projects/[project-name]/2_interview/interview_transcript.md`

## 2.1: Build the Interview Plan

Once a topic is selected, the panel **collectively** designs a custom interview plan:

**1. Identify the narrative arc.** What are the natural acts/chapters of this story?
   - Example: "Before / During / After" or "The Setup / The Crisis / The Resolution"

**2. Assign each interviewer an angle** based on what they'll uniquely extract:

| Interviewer | Their Angle for This Topic |
|-------------|---------------------------|
| Tim Ferriss | [What tactical/mechanical elements will he extract?] |
| Joe Rogan | [What stories/experiences will he pull out?] |
| Larry King | [What core truths will he cut to?] |
| Howard Stern | [What uncomfortable/unspoken things will he reveal?] |
| Michael Barbaro | [What timeline/clarity will he establish?] |
| Barbara Walters | [What emotional depth will she uncover?] |

**3. Create 12-15 questions** organized by the narrative arc, with each interviewer assigned to specific questions based on their strengths.

**4. Present the full interview plan** to the user before beginning.

---

## 2.2: The Interview (One Question at a Time)

**CRITICAL: This is a conversational interview, not a questionnaire.**

- Ask ONE question at a time
- Wait for the user's response
- The NEXT interviewer reads the previous response and uses it to inform their follow-up
- Questions can deviate from the plan if the conversation surfaces something more interesting
- Follow the thread—if the user reveals something unexpected, pursue it

**The flow:**
```
Interviewer 1 asks Question 1
     ↓
User responds
     ↓
Panel evaluates: Is this specific enough? Are there stories, examples, data?
     ↓
If NO → Same or different interviewer pushes deeper
If YES → Next interviewer asks next question (informed by the answer)
     ↓
... and so on
```

---

### CRITICAL: Push for Specificity

**The panel is NEVER satisfied with vague answers.** After each response, evaluate:

| Check | What to Look For |
|-------|------------------|
| **Stories** | Did they share a specific moment with a beginning, middle, end? Names, places, dialogue? |
| **Examples** | Did they give concrete instances, not abstractions? |
| **Data/Numbers** | Are there specific figures, dates, timeframes, metrics? |
| **Sensory Details** | Can you picture it? What did it look like, feel like, sound like? |
| **Emotion** | Did they name the actual feeling, not just describe the situation? |

**If the answer is vague, PUSH BACK with follow-ups like:**

- "You said [X]—can you give me a specific example of when that happened?"
- "What's a moment that captures that? Walk me through it."
- "You're being abstract. Tell me about ONE time this was true."
- "What did that actually look like day-to-day? Be specific."
- "Give me the scene. Where were you? Who was there? What was said?"
- "You said it was 'hard'—what does hard mean? What were the symptoms?"
- "That's the headline. What's the story underneath it?"
- "I want the details. Names, numbers, dates."

**The interview doesn't move forward until the panel has extracted:**
- At least 2-3 specific stories with real details
- Concrete examples that bring abstract points to life
- Numbers/data where relevant (timeframes, metrics, amounts)
- Emotional specificity (not "it was tough" but "I felt like a fraud every morning")

**Only when satisfied does the next planned question get asked.**

**Interviewer styles to maintain:**

- **Tim Ferriss:** Tactical, specific. "Walk me through exactly..." "What's the actual process?"
- **Joe Rogan:** Casual, curious. "That's crazy." "What was going through your head?"
- **Larry King:** Short, direct. "Why?" "What surprised you?"
- **Howard Stern:** Probing, personal. "Be honest..." "The part you don't say publicly..."
- **Michael Barbaro:** Clarifying, structured. "Help me understand..." "Walk me through the timeline..."
- **Barbara Walters:** Emotional, reflective. "What did that teach you?" "How did that feel?"

---

## Interview Tips for the User

1. **Answer in detail.** The more you share, the richer the raw material.
2. **Don't self-edit.** Say the thing you're hesitant to say—that's usually the gold.
3. **Tell specific stories.** Names, dates, places, dialogue make content memorable.
4. **It's a conversation, not a questionnaire.** Each question builds on your previous answer.
5. **Go where the energy is.** If something unexpected comes up, the panel will follow it.
6. **Sit with the hard questions.** Howard and Barbara's questions are uncomfortable for a reason—that's where the best content lives.

---

# STEP 3: PRODUCTION (Create the Raw File)

**Goal:** Transform the interview into a single raw .md file that serves as the source of truth for all content pieces.

**Output location:** `projects/[project-name]/3_production/[topic]_raw.md`

After the interview is complete, synthesize into a raw production file:

```markdown
# [TOPIC TITLE] — Raw Production File

**Interview Date:** [date]
**Topic:** [one-line description]

---

## KEY STORIES EXTRACTED

### Story 1: [Title]
[Full story with details, quotes, specifics as told in interview]

### Story 2: [Title]
[Full story with details, quotes, specifics as told in interview]

### Story 3: [Title]
[Full story with details, quotes, specifics as told in interview]

---

## CORE INSIGHTS

1. [Insight with supporting detail]
2. [Insight with supporting detail]
3. [Insight with supporting detail]

---

## QUOTABLE MOMENTS

> "[Direct quote from interview]"

> "[Direct quote from interview]"

> "[Direct quote from interview]"

---

## EMOTIONAL ANCHOR

[The deeper human truth or feeling that connects everything]

---

## SURPRISING REVEALS

- [Things that came out that weren't expected]
- [Uncomfortable truths shared]
- [Contrarian angles that emerged]

---

## THE "SO WHAT?"

[Why this matters to the reader. The universal resonance.]

---

## RAW INTERVIEW TRANSCRIPT

[Include key excerpts from the interview, preserving the user's exact words]

---

*This raw file is the source of truth for all content derived from this interview.*
```

**IMPORTANT:** This raw file preserves the user's actual words and stories. All content pieces in Step 4 will draw from this source.

Once the raw file is created → Move to Step 4.

---

# STEP 4: REFINEMENT (Draft Content Pieces)

**Goal:** Transform the raw production file into polished content pieces using the user's writing style.

**Output location:** `projects/[project-name]/4_refinement/[platform]_draft.md`

## 4.1: Select Content Types

Ask the user which content types they want created:

```
Which content pieces should we create from this raw material?

□ Newsletter (~1000-1500 words)
□ LinkedIn post (~700 words)
□ X/Twitter thread (10-15 tweets)
□ YouTube script (~2000 words)
□ Blog post (~1500-2000 words)
□ Other: ___________

Select all that apply.
```

## 4.2: Apply the Writing Style Guide

**CRITICAL:** Before drafting, read `style-guide.md` in the root of this folder.

Extract and apply:
- **Voice characteristics** (tone, formality, personality)
- **Structural patterns** (how they open, transition, close)
- **Linguistic fingerprints** (phrases they use, punctuation style)
- **Hook formulas** they prefer
- **Platform-specific patterns**
- **THE #1 RULE:** Write like you're texting a friend

**If no style guide exists:** Ask the user if they want to create one.

## 4.3: Draft Each Content Piece

For each selected content type, draft using:

1. **Raw material** from the production file (Step 3)
2. **Writing style** from style-guide.md
3. **Platform conventions** appropriate to each format

### Platform Guidelines

| Platform | Length | Style Focus |
|----------|--------|-------------|
| Newsletter | ~1000-1500 words | Story-driven, personal, conversational |
| LinkedIn | ~700 words | Professional insight, actionable, pattern-interrupt hook |
| X/Twitter | 10-15 tweets | Punchy, hook-heavy, one idea per tweet |
| YouTube | ~2000 words | Spoken rhythm, clear transitions, visual language |
| Blog | ~1500-2000 words | Comprehensive, structured, evergreen |

### Drafting Principles

- **Preserve the user's actual words** whenever possible
- Draw stories and quotes directly from the raw file
- Match their voice DNA exactly
- Only add new words when absolutely necessary for flow
- Maintain their specific style patterns (lowercase? Short sentences? Specific punctuation?)

## 4.4: Output Format

For each content piece, save to `4_refinement/[platform]_draft.md`:

```markdown
# Step 4: Refinement — [Platform] Draft

**Platform:** [Platform]
**Word Count:** [X]
**Style Applied:** style-guide.md

---

[FULL DRAFT HERE]

---
```

Once drafts are complete → Move to Step 5.

---

# STEP 5: EDITING (Writer's Council Review)

**Goal:** Get expert feedback from 6 world-class writers on the drafted content.

**Output location:** `projects/[project-name]/5_editing/council_review.md`

## The Council Members

| Writer | Superpower | Key Question |
|--------|-----------|--------------|
| **Morgan Housel** | Timelessness & Story | "Will this matter in 10 years?" |
| **Tim Urban** | Clarity & Delight | "Is this confusing anywhere?" |
| **Shaan Puri** | Hooks & Virality | "Would I stop scrolling?" |
| **Greg Isenberg** | Actionability | "What can someone steal?" |
| **David Perell** | Internet Writing Craft | "Is this POP?" |
| **Slop Detector** | AI Authenticity | "Could a machine have written this?" |

## Council Review Process

Run through each council member's lens:

### 1. MORGAN HOUSEL (Timelessness & Depth)

**Reviews for:** Will this matter in 10 years? Is there a deeper human truth? Does it use story effectively?

**Output:**
- What's Working: [strength through his lens]
- What Needs Work: [weakness through his lens]
- Specific Suggestion: [concrete recommendation]
- Timelessness Rating: /10

---

### 2. TIM URBAN (Clarity & Intellectual Delight)

**Reviews for:** Is this confusing anywhere? Could concepts be named? Is this delightful to read?

**Output:**
- What's Working: [strength through his lens]
- Confusion Alert: [where readers might get lost]
- Concept to Name: [idea that deserves a memorable name]
- Clarity Rating: /10

---

### 3. SHAAN PURI (Hooks & Virality)

**Reviews for:** Would I stop scrolling? Does this create OMG, WTF, or LOL?

**Output:**
- Scroll-Stop Test: [Yes/No + why]
- Current Hook Problem: [what's wrong]
- 3 Alternative Hooks: [options]
- Virality Rating: /10

---

### 4. GREG ISENBERG (Actionability & Tactical Value)

**Reviews for:** Can someone use this TODAY? What can they steal?

**Output:**
- Steal Test: [what would someone screenshot?]
- Missing Tactical Element: [what's not actionable enough]
- Framework Suggestion: [how to restructure]
- Actionability Rating: /10

---

### 5. DAVID PERELL (Internet Writing Craft)

**Reviews for:** Is this POP (Personal, Observational, Playful)?

**POP Framework:**
- **Personal:** Stories, emotions, vulnerability
- **Observational:** Hidden truths, patterns others miss
- **Playful:** Wit, analogies, moments of delight

**Output:**
- POP Score: Personal __/10 | Observational __/10 | Playful __/10
- Key Idea (one sentence): [state it or note if missing]
- Internet Writing Rating: /10

---

### 6. SLOP DETECTOR (AI Authenticity Auditor)

**Reviews for:** Does this read as unmistakably human?

**Red flag phrases:** "delve," "landscape," "game-changer," "it's worth noting," "in today's fast-paced world," "leverage," "robust," "seamless"

**Output:**
- Slop Score: /10 (10 = fully human, 1 = pure AI slop)
- Red Flag Phrases Found: [list any]
- Lines That Feel Human: [2-3 lines that work]
- Priority Slop Fixes: [exact text + fix]

---

## Final Synthesis

**Consensus Points:** [Where 2+ agreed]

**Priority Fixes (Ranked):**
1. [Most important - source]
2. [Second - source]
3. [Third - source]

**Overall Score:** /10

**One-Line Verdict:** [The single most important thing this piece needs]

---

# STEP 6: REVISION LOOP (Iterate to 9/10)

**Goal:** Iteratively improve content until the Writer's Council scores it 9/10 or higher.

**Output location:** `projects/[project-name]/6_final/FINAL_[platform].md`

## The Loop Process

```
Council Review → Score < 9? → Gather Info → Revise → Re-Review
                                   ↑                      ↓
                                   └──────────────────────┘

When Score ≥ 9/10 → Save to 6_final/
```

**6.1: Check Score**
- If Overall Score ≥ 9/10 → STOP. Save final draft to `6_final/`.
- If Overall Score < 9/10 → Continue to 6.2.

**6.2: Gather Information (if needed)**

Before revising, ask the user for:
- Story details (names, quotes, specific moments)
- Clarification on unclear points
- Which council feedback to prioritize

**6.3: Revise**

Rewrite the draft addressing the Priority Fixes from the council.

**CRITICAL:** Maintain the author's voice from style-guide.md.

**6.4: Re-Review**

Run the council again. Note what improved and what still needs work.

**6.5: Loop**

Repeat until score ≥ 9/10 or maximum 3 revision cycles.

---

### Final Output

When approved, save to `6_final/FINAL_[platform].md`:

```markdown
# FINAL: [Platform] Version

**Status:** ✓ Approved (9/10)
**Platform:** [Platform]

---

[FULL FINAL DRAFT HERE]

---

*Generated via The Content Machine*
```

---

## Pro Tips

1. **The raw file is sacred.** Step 3's production file preserves the user's actual words. Don't paraphrase away the gold.
2. **Style guide is mandatory.** Step 4 requires applying the user's voice from style-guide.md.
3. **Hook-first workflow:** If Shaan's review fails in Step 5, nothing else matters.
4. **Tension is information:** When Morgan and Shaan disagree, that reveals the depth vs. virality tradeoff.
5. **Ask before assuming:** In Step 6, if you need more context to make a revision, ask the user.
6. **9/10 is the bar.** Don't ship until the council agrees it's ready.

---

*Built by Alex Lieberman. The Content Machine: Input → Interview → Production → Refinement → Editing → Revision.*
