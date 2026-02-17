---
name: content-machine
description: A complete content creation system. The Oracle mines your apps for content seeds → Interview Panel extracts your stories → Raw production file → Refinement with your writing style → Writer's Council editing → Revision loop until 9/10.
---

# The Content Machine

A complete system for creating publish-ready content from your ideas.

```
┌─────────────────────────────────────────────────────────────────────┐
│                        THE CONTENT MACHINE                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  STEP 1: THE ORACLE     → Mines Slack/Notion for content spikes     │
│            ↓                                                        │
│  STEP 2: INTERVIEW      → Panel extracts stories, insights, data    │
│            ↓                                                        │
│  STEP 3: PRODUCTION     → Interview → raw .md file (source of truth)│
│            ↓                                                        │
│  STEP 4: REFINEMENT     → Select content type, draft with style     │
│            ↓                                                        │
│  STEP 5: EDITING        → Writer's Council reviews and scores       │
│            ↓                                                        │
│  STEP 6: REVISION LOOP  → Iterate until 9/10                        │
│                                                                     │
│  Content types are modular — each type has its own spec in          │
│  content-types/. Types with custom pipelines (e.g., playbook)       │
│  define their own steps instead of using Steps 1-6.                 │
│                                                                     │
│  ─── LEARNING LOOP ───                                              │
│                                                                     │
│  --learn [project]      → Diff draft vs final, extract lessons      │
│  --learn --verbal       → Direct feedback → structured lessons      │
│  Auto-prompted          → Offered after every 9/10 approval         │
│    ↓                                                                │
│  content-lessons.md     → Read alongside style guides on next draft  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## System Structure

```
/content-machine/
├── .claude/
│   └── commands/
│       └── content-machine.md  ← You are here (the process)
├── config.md                   ← Your settings (Slack ID, Oracle channel)
├── style-guide.md              ← Your writing voice
├── content-lessons.md          ← Accumulated lessons from feedback
├── content-types/
│   ├── _template.md            ← Template for creating new content types
│   ├── long-post.md            ← Long-form post spec
│   ├── linkedin-post.md        ← LinkedIn post spec
│   ├── x-thread.md             ← X/Twitter thread spec
│   └── playbook.md             ← Playbook pipeline + format spec
├── scripts/
│   ├── fetch-transcript.sh     ← YouTube transcript fetcher
│   └── daily-oracle.sh         ← Automated daily Oracle scanner
├── projects/
│   └── [project-name]/
│       ├── 1_oracle/           ← Topic discovery from apps
│       ├── 2_interview/        ← Interview transcript
│       ├── 3_production/       ← Raw .md file (source of truth)
│       ├── 4_refinement/       ← Platform drafts
│       ├── 5_editing/          ← Council review
│       └── 6_final/            ← Approved versions
└── oracle-reports/             ← Oracle output
```

---

## Quick Commands

**First-Time Setup:**
```
/content-machine --setup
```

**Full Pipeline (Steps 1-6):**
```
/content-machine --full [topic]
/content-machine --full (no topic - Oracle finds one)
```

**New Project:**
```
/content-machine --new [project-name]
```

**The Oracle Only (Step 1):**
```
/content-machine --oracle
/content-machine --oracle --slack (Slack only)
/content-machine --oracle --notion (Notion only)
/content-machine --oracle --daily (last 24 hours, for automated runs)
```

**Start from Interview (Steps 2-4):**
```
/content-machine --interview [topic]
/content-machine --interview
```

**Content Type Shortcuts (skip Step 4.1 selection):**
```
/content-machine --long-post [topic]
/content-machine --linkedin [topic]
/content-machine --x-thread [topic]
/content-machine --playbook [YouTube URL]
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

**Learn from Feedback:**
```
/content-machine --learn [project-name]
/content-machine --learn (most recent project)
/content-machine --learn --verbal "your feedback"
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
├── 1_oracle/
├── 2_interview/
├── 3_production/
├── 4_refinement/
├── 5_editing/
└── 6_final/
```

All files for this content piece live in this folder, organized by step.

---

## The Teams

### The Oracle (Step 1)

The Oracle is your content discovery engine. It connects to your apps and mines for **spikes**—moments where you naturally created something worth sharing.

| Source | What It Mines |
|--------|---------------|
| **Slack** | DMs, channels, threads where you shared a strong take |
| **Notion** | Notes, docs, meeting notes with buried insights |

**What The Oracle Looks For:**
- **Strong POVs** — Contrarian opinions, bold statements, things you believe that others don't
- **Stories** — Specific moments, anecdotes, experiences you've mentioned
- **Examples/Lessons** — Frameworks, lessons learned, tactical insights
- **Emotional Spikes** — Frustrations, excitements, rants, celebrations

**MCP Server Requirements:**
The Oracle requires MCP servers to connect to your apps:
- `slack` — Anthropic's Slack MCP server
- `notion` — Notion MCP server

---

### The Interview Panel (Step 2)

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

# STEP 1: THE ORACLE (Topic Discovery)

**Goal:** Mine your connected apps for content "spikes"—moments where you naturally said something worth expanding.

**Output location:** `projects/[project-name]/1_oracle/oracle_findings.md`

If the user already has a topic, skip to Step 2.

---

## 1.1: Connect to Sources

The Oracle connects to:

| Source | What to Search | Spike Signals |
|--------|----------------|---------------|
| **Slack** | DMs, key channels, threads from last 30 days | Strong language, long messages, threads you started, rants, teaching moments |
| **Notion** | Recent docs, meeting notes, personal notes | Bullet points with conviction, "here's what I learned", frameworks you created |

**MCP commands used:**
- Slack: Search messages, read threads, scan channels
- Notion: Search pages, read content blocks

**Configuration:** Read `config.md` for the user's Slack User ID and Oracle channel settings. Time range is configurable (default: 30 days).

---

## 1.1.1: Automated Oracle Process

When running the Oracle automatically (e.g., `--daily` or `--oracle`), follow this exact process:

**Step 1: Get all channels the bot has access to**
```
mcp__slack__slack_list_channels
```

**Step 2: For each channel, pull recent messages**
```
mcp__slack__slack_get_channel_history (limit: 100 per channel)
```

**Step 3: Filter for the user's messages only**
- User ID: Read from `config.md`
- Time range: Default last 30 days (or last 24 hours for `--daily`)

**Step 4: Score each message against spike criteria**

For each message, calculate scores (0-10) for:

| Criteria | What to Look For | Score Signals |
|----------|------------------|---------------|
| **POV Strength** | Contrarian take, bold claim, defended opinion | "I think...", "Actually...", "Here's why...", disagreement, strong language |
| **Story Potential** | Specific moment, characters, conflict, emotion | Names, dates, places, "Let me tell you...", "What happened was...", dialogue |
| **Emotional Intensity** | Frustration, excitement, passion, vulnerability | Rants, exclamation points, caps, strong reactions |
| **Lesson/Framework** | Teaching moment, process, how-to | "The way I think about...", "Here's the process...", numbered steps, "I learned..." |
| **Length/Depth** | Longer messages = more developed thought | Word count > 50, multiple paragraphs, threads with replies |

**Composite Spike Score:** Average of all criteria, weighted by:
- POV Strength: 25%
- Story Potential: 25%
- Emotional Intensity: 20%
- Lesson/Framework: 20%
- Length/Depth: 10%

**Step 5: Return ranked spikes**
- Only include messages with Spike Score >= 6/10
- Rank by composite score descending
- Include raw message text + thread context if available

**Step 6: Post to Slack (for --daily runs)**

When running with `--daily` flag, automatically post a digest to the Oracle channel configured in `config.md`:

```
DAILY ORACLE — [Date]

Scanned [X] messages from the last 24 hours.

**Top Spikes Found:**

1. **[Title]** (Score: X/10)
   > "[First 100 chars]..."

2. **[Title]** (Score: X/10)
   > "[First 100 chars]..."

3. **[Title]** (Score: X/10)
   > "[First 100 chars]..."

[If no spikes >= 6: "No high-scoring spikes today. Keep sharing your thoughts!"]

Full report saved locally. Reply to develop any spike into content.
```

Use `mcp__slack__slack_post_message` with the channel ID from `config.md`.

---

## 1.2: Identify Spikes

A "spike" is content that already has energy. Look for:

### Strong POVs
- Contrarian opinions ("I actually think X is wrong...")
- Bold predictions ("This is going to...")
- Unpopular takes defended with reasoning

### Stories
- Specific moments with characters, settings, conflict
- "Let me tell you what happened..."
- Behind-the-scenes explanations

### Examples/Lessons
- Tactical frameworks you've explained
- Lessons from failures or wins
- "The way I think about this is..."

### Emotional Spikes
- Frustration rants (these often contain your best material)
- Excitement about something new
- Strong reactions to industry events

---

## 1.3: Surface Topics

Present 5-6 spikes as potential content topics, ranked by spike score:

**Output format:**
```
THE ORACLE — Content Spikes Found

Scanned: [X] channels | Time range: [last N days] | Messages analyzed: [Y]

## RANKED SPIKES

### SPIKE 1: "[Short title from message]"
**Spike Score:** 8.5/10
| POV: 9 | Story: 8 | Emotion: 8 | Lesson: 9 | Depth: 8 |

**Source:** #[channel] — [date]
**Raw excerpt:**
> "[First 200 chars of message]..."

**Why it works:** [Brief explanation of content potential]

---

### SPIKE 2: "[Short title]"
**Spike Score:** 7.8/10
| POV: 7 | Story: 9 | Emotion: 8 | Lesson: 7 | Depth: 8 |

**Source:** #[channel] — [date]
**Raw excerpt:**
> "[First 200 chars]..."

**Why it works:** [Brief explanation]

[...continue for top 5-6 spikes with score >= 6]

---

**What do you want to do?**

1. **Pick a spike** — Reply with the number (e.g., "1" or "Spike 1")
2. **None of these** — Reply "none" to enter Discovery Mode
3. **I have my own idea** — Just describe it and we'll skip to the interview

```

---

## 1.3.1: Discovery Mode (No Spike Fallback)

When none of the spikes resonate, present these 4 paths:

```
None of these spikes hitting? No problem. Pick a path:

**PATH 1: Quick-Fire Questions** (Recommended)
I'll ask you 5 rapid questions to surface what's actually on your mind.

**PATH 2: Category Menu**
Pick a content category (contrarian take, mistake + lesson, framework, etc.) and I'll help you find an angle.

**PATH 3: Trending Topics**
Tell me a topic area you care about and I'll pull what's trending that you could riff on.

**PATH 4: Bypass — I Know My Topic**
Already know what you want to talk about? Just tell me and we'll jump to the interview.

Which path? (1, 2, 3, or 4)
```

---

### Path 1: Quick-Fire Questions

Ask these 5 questions in rapid succession (one at a time, short answers encouraged):

1. **"What frustrated you this week?"**
   - Rants often contain your best material

2. **"What did you explain to someone recently?"**
   - Teaching moments = content

3. **"What's a belief you hold that most people disagree with?"**
   - Contrarian POVs stand out

4. **"What changed your mind recently?"**
   - Evolution stories resonate

5. **"What's working right now that you haven't talked about publicly?"**
   - Untold wins are gold

**After collecting answers:**
- Synthesize 2-3 topic angles from their responses
- Present as mini-spikes with one-line descriptions
- User picks one → hand off to Interview Panel

---

### Path 2: Category Menu

Present these categories and let the user pick:

```
Pick a category that feels right:

1. **Contrarian Take**
   "What do you believe that most people in your industry think is wrong?"

2. **Mistake + Lesson**
   "What's a mistake you made in the last year that taught you something?"

3. **System/Framework**
   "What's a process you use that others should steal?"

4. **Prediction**
   "What do you think is going to happen in the next 2-3 years that others aren't seeing?"

5. **Behind the Scenes**
   "What's something going on in your business right now that would surprise people?"

6. **Rant/Frustration**
   "What's something in your industry that pisses you off that no one talks about?"

Which category? (1-6)
```

**After user picks a category:**
- Ask 1-2 follow-up questions to sharpen the angle
- Confirm the topic
- Hand off to Interview Panel

---

### Path 3: Trending Topics

**Step 1:** Ask the user for a topic area:
```
What topic area do you want to explore? (e.g., "AI and startups", "content creation", "hiring", "fundraising", "leadership")
```

**Step 2:** Use web search to find trending stories, posts, and conversations in that space from the last 7 days.

**Step 3:** Present 3-5 trending angles:
```
TRENDING IN [TOPIC AREA] — Last 7 Days

1. **[Trending topic/story]**
   What's happening: [1-2 sentence summary]
   Your angle: [How you could riff on this based on your experience]

2. **[Trending topic/story]**
   What's happening: [1-2 sentence summary]
   Your angle: [How you could riff on this]

3. **[Trending topic/story]**
   What's happening: [1-2 sentence summary]
   Your angle: [How you could riff on this]

Which one sparks something? Or tell me what angle you'd take.
```

**Step 4:** User picks a trend or provides their own angle → hand off to Interview Panel

---

### Path 4: Bypass — User Provides Topic

If the user already knows their topic:
- Confirm: "Got it — we're going with **[their topic]**"
- Skip directly to Step 2 (Interview)
- No additional Oracle work needed

---

## 1.4: Save Oracle Findings

Save to `1_oracle/oracle_findings.md`:

```markdown
# Oracle Findings — [Date]

## Scan Summary
- **Time range:** [last N days]
- **Channels scanned:** [list]
- **Total messages analyzed:** [X]
- **Spikes found (score >= 6):** [Y]

## Ranked Spikes

### Spike 1: [Topic]
- **Spike Score:** [X]/10
- **Breakdown:** POV: [X] | Story: [X] | Emotion: [X] | Lesson: [X] | Depth: [X]
- **Source:** #[channel] — [date]
- **Raw excerpt:** "[direct quote from source]"
- **Thread context:** [if any replies, summarize]
- **Content potential:** [brief notes]

[...continue for all spikes >= 6]

## Selected Topic
[Topic chosen by user]
```

## 1.5: Oracle → Interview Handoff

After presenting spikes, wait for user response:

**If user picks a spike (e.g., "1", "Spike 2"):**
1. Confirm the selection: "Got it — we're going with **[Topic]**"
2. Pull the raw excerpt and any thread context from that spike
3. Automatically transition to Step 2 (Interview) with this context
4. The Interview Panel receives: topic + original message + any thread replies

**If user says "none" or "I don't like these":**
1. Enter Discovery Mode (see Section 1.3.1)
2. Present the 4 paths and let user choose
3. Follow the selected path to surface a topic
4. When a topic emerges, confirm it and transition to Step 2

**If user provides their own topic (Path 4 — Bypass):**
1. Confirm: "Got it — we're going with **[their topic]**"
2. Transition directly to Step 2 (no additional Oracle work needed)

**Handoff message to Interview Panel:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ORACLE → INTERVIEW HANDOFF

**Topic:** [Selected topic]
**Source:** [Spike source if applicable, or "User-provided"]
**Raw material:**
> [Original message/excerpt if from spike]

**Thread context:** [Any replies or discussion if available]

The Interview Panel will now extract stories, insights, and details.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Then immediately begin Step 2.1 (Build the Interview Plan).

---

# STEP 2: INTERVIEW (Extract the Raw Material)

**Goal:** Extract stories, insights, examples, and data through a conversational interview.

**Output location:** `projects/[project-name]/2_interview/interview_transcript.md`

The Interview Panel takes the topic selected via The Oracle (or provided directly by the user) and conducts a deep-dive interview.

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
- "That's the headline. What's the story underneath it."
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

Read the `content-types/` directory and present available content types to the user.

For each `.md` file in `content-types/` (excluding `_template.md`), read the Overview section to get the one-line description.

Present them as a selection:

```
Which content pieces should we create from this raw material?

Available content types:
□ Long Post — Story-driven long-form post (1,000-2,500 words)
□ LinkedIn Post — Professional-casual LinkedIn post (3,000 char max)
□ X Thread — Punchy, hook-heavy X/Twitter thread (10-15 tweets)
□ Playbook — Tactical playbook from YouTube expert interview
[...any additional content types found in content-types/]

Select all that apply. Or suggest a new content type.
```

**If a content-type-specific flag was used** (e.g., `--long-post`, `--linkedin`):
Skip this selection — the content type is already chosen. Read its spec file directly.

**If the selected content type has `Pipeline: custom`:**
Follow the custom pipeline defined in the content type spec file instead of continuing with Steps 4-6.

## 4.2: Apply the Writing Style Guide + Lessons

**CRITICAL:** Before drafting, read these files in the root of this folder:
1. `style-guide.md` — Your core writing voice
2. `content-lessons.md` — Accumulated lessons from past feedback and edits

**If a lesson in `content-lessons.md` conflicts with `style-guide.md`, the lesson takes priority** — it represents newer, specific learning.

Extract and apply:
- **Voice characteristics** (tone, formality, personality)
- **Structural patterns** (how they open, transition, close)
- **Linguistic fingerprints** (phrases they use, punctuation style)
- **Hook formulas** they prefer
- **Platform-specific patterns**
- **Lessons learned** from past projects (corrections, preferences, anti-patterns)
- **Apply the core voice rule from your style-guide.md** — whatever the #1 writing principle is.

**If no style guide exists:** Ask the user if they want to create one (run `--setup`).

## 4.3: Draft Each Content Piece

For each selected content type:

1. Read the content type spec file from `content-types/`
2. Apply the **Format Specification** and **Drafting Instructions** from the spec
3. Use **raw material** from the production file (Step 3)
4. Apply **writing style** from style-guide.md + content-lessons.md

### Drafting Principles

- **Preserve the user's actual words** whenever possible
- Draw stories and quotes directly from the raw file
- Match their voice DNA exactly
- Only add new words when absolutely necessary for flow
- Maintain their specific style patterns
- Check the content type spec for platform-specific formatting rules

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

**NOTE:** Some content types define modified council criteria (see the "Council Adaptations" section in the content type spec). If the selected content type has council adaptations, use those instead of the default criteria below.

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

**Status:** Approved (9/10)
**Platform:** [Platform]

---

[FULL FINAL DRAFT HERE]

---

*Generated via The Content Machine*
```

### 6.6: Learn from This Project (Optional)

After saving the final draft, offer to learn from the revision history:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONTENT APPROVED — Saved to 6_final/

Want me to learn from this project's revision history?
This captures what the council kept flagging so future first drafts start stronger.

→ Learn now? (y/n)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

If yes: Run the `--learn` flow using the current project — compare the Step 4 draft against the Step 6 final, analyze council feedback patterns, extract candidate lessons, present for user confirmation, and update `content-lessons.md`.

If no: Skip. User can always run `/content-machine --learn [project-name]` later.

---

## Pro Tips

1. **The raw file is sacred.** Step 3's production file preserves the user's actual words. Don't paraphrase away the gold.
2. **Style guide is mandatory.** Step 4 requires applying the user's voice from style-guide.md.
3. **Hook-first workflow:** If Shaan's review fails in Step 5, nothing else matters.
4. **Tension is information:** When Morgan and Shaan disagree, that reveals the depth vs. virality tradeoff.
5. **Ask before assuming:** In Step 6, if you need more context to make a revision, ask the user.
6. **9/10 is the bar.** Don't ship until the council agrees it's ready.

---

# CUSTOM CONTENT TYPE PIPELINES

Some content types define their own custom pipeline instead of using Steps 1-6. When a content type's spec file has `Pipeline: custom`, follow the pipeline defined in that file.

**Currently available custom pipelines:**
- **Playbook** (`content-types/playbook.md`) — YouTube → Transcript → Extraction → Draft → Playbook Council → Revision

To invoke a custom pipeline directly:
```
/content-machine --playbook [YouTube URL]
```

---

# SETUP (First-Time Configuration)

**Command:** `/content-machine --setup`

Walks a new user through configuring the Content Machine.

---

## Setup Step 1: Create Your Style Guide

Present three options:

**Option A: Analyze your existing content**
"Share 10-20 of your best-performing posts (any platform). Paste them here or point me to a file. I'll analyze your voice, hook patterns, structural preferences, and linguistic fingerprints."

Process:
1. User provides posts
2. Analyze using style-guide.example.md as the template structure:
   - Voice characteristics
   - Hook formulas (with examples from their content)
   - Content structures
   - Linguistic fingerprints (signature phrases, punctuation)
   - Platform-specific patterns
   - Do's and Don'ts
3. Present draft style guide for review
4. Save to style-guide.md

**Option B: Interview about your voice**
Ask 10 questions (one at a time):
1. "Share a post you're proud of. What makes it you?"
2. "How formal is your writing? (texting a friend → academic paper)"
3. "Do you use profanity? Slang? Abbreviations?"
4. "What's your relationship with punctuation? Short sentences or long ones?"
5. "What words do you overuse? What do you never say?"
6. "How do you typically open a post? What hooks feel natural?"
7. "What content structures do you gravitate toward? Lists? Stories? Arguments?"
8. "What platforms do you write for? How does your voice change between them?"
9. "Share a post by someone else whose style you admire. What specifically?"
10. "What's the one thing an AI writing in your voice always gets wrong?"

Synthesize into style-guide.md.

**Option C: Start blank and build as you go**
Create style-guide.md with section headers and placeholders. The Learning Loop fills it in as you create content.

---

## Setup Step 2: Configure Your Apps

"Do you use any of these? (select all that apply)
- Slack
- Notion"

For Slack:
1. Ask for Slack User ID (explain how to find it: Slack profile → three dots → Copy member ID)
2. Ask for Oracle channel name and ID (or "none" to skip auto-posting)
3. Verify MCP server is installed

For Notion:
1. Verify MCP server is installed

Save settings to config.md.

---

## Setup Step 3: Review Content Types

List all available content types from `content-types/` with their one-line descriptions.

"You can use these as-is, edit any to match your format, or create new ones using content-types/_template.md."

---

## Setup Step 4: Confirm

```
Setup complete!

Style guide: [created / skipped]
Apps: [Slack / Notion / none]
Content types: [X] available
Lessons file: Empty (will learn from your feedback)

Try:
  /content-machine --oracle           (find content spikes)
  /content-machine --full [topic]     (full pipeline)
  /content-machine --playbook [URL]   (playbook from YouTube)
```

---

# LEARNING FROM FEEDBACK

The Content Machine learns from your edits, feedback, and revision patterns to improve future first drafts.

```
┌─────────────────────────────────────────────────────────────────────┐
│                       LEARNING LOOP                                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  TRIGGER 1: --learn [project]   → Diff draft vs final, extract      │
│  TRIGGER 2: Auto-prompt         → Offered at end of Step 6          │
│  TRIGGER 3: --learn --verbal    → Direct feedback from user          │
│                                                                      │
│  OUTPUT: content-lessons.md     → Read alongside style guides        │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

## Quick Commands

```
/content-machine --learn [project-name]     ← Learn from a specific project
/content-machine --learn                    ← Learn from most recent project
/content-machine --learn --verbal "..."     ← Learn from direct feedback
```

---

## The --learn Process

### When invoked with a project name (or most recent project):

**Step L1: Locate the artifacts**

Find and read these files from the project:
1. The **initial draft** — `4_refinement/*_draft.md` or the draft from a custom pipeline
2. The **council review** — `5_editing/council_review.md` or the review from a custom pipeline
3. The **final approved version** — `6_final/FINAL_*.md` or the final from a custom pipeline
4. The **user's published version** (if it exists) — check `finished_posts/` and `finished_content/` for a file matching this project
5. The **current lessons file** — `content-lessons.md`

**Step L2: Semantic diff analysis**

Compare the initial draft against the final version (or the user's published version if it differs from the system's final). This is NOT a literal character diff. Identify:

- **Structural changes:** Did sections get reordered, cut, or added?
- **Voice corrections:** Did tone, formality, or word choice shift?
- **Hook modifications:** Was the opening rewritten?
- **Cuts:** What did the revision remove? (Signals the system over-generated)
- **Additions:** What was added? (Signals the system missed something)
- **Phrasing substitutions:** What specific phrases were replaced, and what pattern does that reveal?

For each detected change, formulate a candidate lesson:

```
**[Category]:** [Lesson statement — what to do differently next time]
- Source: [project-name], [date]
- Evidence: System wrote "[original]" → Changed to "[edited]"
- Confidence: Low (first observation)
```

**Step L3: Council pattern analysis**

Read the council review(s) from this project. Cross-reference against existing lessons in `content-lessons.md`. Look for:

- Feedback that appeared in **multiple projects** (the system keeps making the same mistake)
- Categories that consistently score low
- Specific phrases the Slop Detector flagged
- Revision suggestions that were successfully applied

**Step L4: Present candidate lessons for confirmation**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LEARNING FROM: [project-name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

I analyzed the revision history and found [N] potential lessons:

LESSON 1 — [Category: Voice & Tone]
"[Lesson statement]"
Evidence: [What changed and why this seems like a pattern]

LESSON 2 — [Category: Structure & Flow]
"[Lesson statement]"
Evidence: [What changed and why]

[...for each candidate]

Which lessons should I save? (all / select by number / none)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**CRITICAL:** The user must confirm before any lesson is saved. The system may extract wrong patterns.

**Step L5: Contradiction check**

Before saving, scan existing lessons in `content-lessons.md` for conflicts with new lessons. If found:

```
NEW: "[new lesson]"
EXISTING: "[conflicting existing lesson]"

These seem to conflict. Which do you want?
1. Keep the new one (replace old)
2. Keep the old one (skip new)
3. Merge into a nuanced rule
```

**Step L6: Save to content-lessons.md**

For each confirmed lesson:
1. Add it to the appropriate section (Voice & Tone, Hooks & Openings, etc.)
2. Include date and source project
3. Set confidence level (Low if first observation, bump to Medium if matches an existing lesson)
4. Update the lesson count and last-updated date in the file header

---

### When invoked with --verbal:

```
/content-machine --learn --verbal "I don't like how the system always makes hooks too long"
```

**Step V1:** Parse the verbal feedback into one or more structured lesson candidates.

**Step V2:** Present candidates for confirmation — the system may have misinterpreted the feedback.

```
I interpreted your feedback as:

LESSON — [Category: Hooks & Openings]
"Keep hooks concise — under 2 lines for social, under 3 sentences for newsletter"
Confidence: Medium (directly stated by user)

Is this what you meant? (yes / edit / no)
```

**Step V3:** Save confirmed lessons to `content-lessons.md` with confidence: Medium (user-stated).

---

## Confidence Levels

| Level | Meaning | How It's Set |
|-------|---------|--------------|
| **Low** | Observed once | First time a pattern appears in a single project |
| **Medium** | Observed twice OR user-stated | Pattern appears in 2 projects, or user gave direct verbal feedback |
| **High** | Observed 3+ times | Pattern confirmed across multiple projects — candidate for graduation |

---

## Keeping content-lessons.md Lean

### 30-Lesson Hard Cap

When adding a lesson would push the total above 30, trigger a review:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSONS FILE AT CAPACITY (30/30)

Before adding new lessons, let's review the existing ones:

[List all current lessons with dates and confidence levels]

For each lesson, choose:
  → GRADUATE to style guide (proven pattern → permanent rule)
  → ARCHIVE (no longer relevant)
  → MERGE with another lesson
  → KEEP as is
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Graduating a lesson** means moving it into `style-guide.md` as a permanent rule, then removing it from `content-lessons.md`. Only graduate High-confidence lessons.

### Periodic Review

Every 5 projects, after completion:

```
You've completed 5 projects since the last lessons review.
Want to review content-lessons.md for stale or graduated lessons? (y/n)
```

Tracked by the "Projects since last review" counter in the `content-lessons.md` header. Increment this counter every time a project reaches final approval (Step 6 or custom pipeline completion).
