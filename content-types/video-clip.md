# Content Type: Video Clip

## Overview

- **Command flag:** `--video-clip [path-to-video.mp4]`
- **Description:** Edits a short-form video with captions, transitions, intro/outro, and brand styling using Remotion. Optionally produces written content (LinkedIn post, X post) from the same transcript.
- **Output:** Rendered .mp4 video + optional written posts
- **Platform:** YouTube Shorts, TikTok, Instagram Reels, X, LinkedIn

---

## Pipeline

**Pipeline: custom**

This content type uses a custom 6-step pipeline (V1-V6) rather than the standard content machine pipeline.

```
V1: INGEST       → Validate video, extract audio, transcribe via Whisper
V2: ANALYZE      → Identify structure, score moments, map timestamps
V3: EDIT PLAN    → Scene breakdown: aspect ratio, captions, transitions, intro/outro
V4: WRITTEN      → (Optional) Draft written posts from the transcript
V5: VIDEO BUILD  → Generate Remotion compositions, preview, render
V6: REVIEW       → User watches preview, provides feedback, iterate
```

---

### STEP V1: INGEST (Validate and Transcribe)

**Goal:** Get a validated video file and a word-level transcript.

**Output location:** `projects/[project-name]/1_transcript/`

#### V1.1: Create Project Folder

When the user provides a video file path, create the project folder:

```
projects/[project-name]/
├── 1_transcript/
│   ├── transcript.json    ← Remotion Caption format (word-level timestamps)
│   └── transcript.md      ← Human-readable text
├── 2_edit_plan/
│   └── edit_plan.md       ← Scene breakdown with timestamps
├── 3_written/             ← Written content drafts (optional)
└── 4_video/
    ├── compositions.md    ← Remotion composition specs
    └── rendered/          ← Final .mp4 output
```

Name the project folder based on the video content (e.g., `cody-schneider-gtm-clip`, `ai-native-marketing-reel`).

#### V1.2: Validate Video

Check:
- File exists and is a supported format (.mp4, .mov, .webm)
- File is accessible (not corrupted)

If validation fails, inform the user and ask for a different file.

#### V1.3: Extract Audio and Transcribe

```bash
# Extract audio as 16KHz WAV (required for Whisper)
ffmpeg -i [input-video] -ar 16000 -ac 1 [project-path]/1_transcript/audio.wav -y

# Transcribe with word-level timestamps
cd video && npx tsx src/lib/transcribe.ts [project-path]/1_transcript/audio.wav [project-path]/1_transcript/transcript.json
```

This produces:
- `transcript.json` — Remotion Caption format with word-level timestamps (used for caption rendering)
- `transcript.md` — Human-readable text (used for written content drafting)

#### V1.4: Transcript Quality Check

Before proceeding, verify:
- Transcript has content (not empty or garbled)
- Audio quality was sufficient for transcription

**If transcription fails:**
1. Inform the user: "Couldn't transcribe the audio automatically."
2. Offer alternatives:
   - "Can you paste a transcript or provide an SRT file?"
   - "Try a video with clearer audio"

Once transcript is saved, move to Step V2.

---

### STEP V2: ANALYZE (Identify Structure and Moments)

**Goal:** Understand the video's content structure and identify the strongest moments.

**Output location:** `projects/[project-name]/2_edit_plan/analysis.md`

#### V2.1: Read and Analyze Transcript

Read the transcript and identify:

- **Natural structure:** Intro, key points, stories, examples, conclusion
- **Speaker patterns:** Who's talking when (if multi-speaker)
- **Topic segments:** Where the subject changes

#### V2.2: Score Moments

For videos over 60 seconds, score sections for "clip-worthiness":

| Criteria | Weight | Signals |
|----------|--------|---------|
| Hook Strength | 30% | Provocative statement, surprising stat, bold claim |
| Insight Density | 25% | Specific frameworks, tools, numbers, actionable advice |
| Emotional Peak | 20% | Strong reactions, humor, passion, frustration |
| Quotability | 15% | Memorable one-liners, screenshot-worthy moments |
| Standalone Quality | 10% | Does this segment make sense without the rest? |

For videos under 60 seconds, treat the entire video as a single clip — skip scoring.

#### V2.3: Map Timestamps

Output a structured analysis:

```markdown
## Video Analysis

**Duration:** [X minutes, Y seconds]
**Speakers:** [List]
**Overall Topic:** [One line]

### Structure Map
- 0:00-0:15 — Intro/Hook: [description]
- 0:15-1:30 — Key Point 1: [description]
- 1:30-2:45 — Key Point 2: [description]
- ...

### Best Moments (ranked by clip-worthiness)
1. [Timestamp range] — "[Quote or description]" — Score: X/10
2. [Timestamp range] — "[Quote or description]" — Score: X/10
3. ...

### Recommended Cuts
- Trim start: [remove first X seconds if slow start]
- Trim end: [remove last X seconds if trailing off]
- Dead spots: [timestamps of filler, "um"s, or dead air]
```

---

### STEP V3: EDIT PLAN (Scene Breakdown)

**Goal:** Define exactly how the video will be edited before building anything.

**Output location:** `projects/[project-name]/2_edit_plan/edit_plan.md`

#### V3.1: Determine Output Format

Ask the user (or infer from video dimensions):

```
What format should the final video be?

□ 9:16 Vertical — TikTok, Instagram Reels, YouTube Shorts
□ 16:9 Horizontal — YouTube, Twitter/X
□ 1:1 Square — Instagram feed, LinkedIn
□ Keep original aspect ratio
```

#### V3.2: Define Edit Plan

Generate a detailed plan covering:

```markdown
## Edit Plan

### Output Specs
- **Aspect Ratio:** [9:16 / 16:9 / 1:1]
- **Resolution:** [1080x1920 / 1920x1080 / 1080x1080]
- **FPS:** 30
- **Estimated Duration:** [X seconds]

### Intro (optional)
- **Duration:** 2-3 seconds
- **Style:** [fade from black / logo reveal / text card]
- **Title Text:** "[Show name or topic]"
- **Logo:** [path in assets/logos/ or "none"]

### Main Content
- **Source:** [full video / trimmed to timestamps]
- **Trim Start:** [timestamp or "none"]
- **Trim End:** [timestamp or "none"]
- **Speed:** [1x / 1.2x / etc.]

### Captions
- **Style:** TikTok word-highlight
- **Position:** Bottom 15%
- **Font:** [Inter / custom from assets/fonts/]
- **Font Size:** [70 for vertical, 50 for horizontal]
- **Highlight Color:** [hex code, e.g., #39E508]
- **Text Color:** White with drop shadow

### Lower Third (optional)
- **Speaker Name:** [name]
- **Speaker Title:** [title]
- **Duration:** First 5 seconds
- **Brand Color:** [hex]

### Outro (optional)
- **Duration:** 2-3 seconds
- **Style:** [fade to black / CTA card]
- **Text:** "[Subscribe / Follow / etc.]"
- **Logo:** [same as intro or "none"]

### Transitions
- **Intro → Main:** [fade / cut]
- **Main → Outro:** [fade / cut]
- **Between segments (if multi-clip):** [fade / slide / cut]
```

#### V3.3: Present Plan for Approval

Present the full edit plan to the user and wait for confirmation before building.

**CRITICAL:** Do not proceed to V5 without user approval on the edit plan. This prevents wasted render time.

---

### STEP V4: WRITTEN CONTENT (Optional, Dual Output)

**Goal:** Draft written posts from the same transcript, if the user wants them.

#### V4.1: Ask the User

```
We have the transcript. Want to also create written content from this video?

□ LinkedIn Post — Promo post with tactical value
□ X Post — Casual post promoting the clip
□ Podcast Promo — Full promo post (if this is a podcast episode)
□ Skip — Video only
```

#### V4.2: Draft Written Content

If selected, follow the existing content type specs:
- Read the relevant content type file from `content-types/`
- Use the transcript from V1 as raw material (same as how playbook uses a YouTube transcript)
- Apply `style-guide.md` + `content-lessons.md`
- Save drafts to `projects/[project-name]/3_written/`

This step runs independently of V5 — it does not need to wait for the video to be built, and the video does not need to wait for written content.

---

### STEP V5: VIDEO BUILD (Remotion Composition + Render)

**Goal:** Generate the Remotion composition code and render the final video.

**Output location:** `projects/[project-name]/4_video/`

#### V5.1: Prepare Assets

```bash
# Copy source video to Remotion's public directory
cp [source-video] video/public/video.mp4

# Copy captions JSON
cp [project-path]/1_transcript/transcript.json video/public/captions.json

# Copy brand assets if used
cp assets/logos/[logo] video/public/logo.png  # if intro/outro uses logo
```

#### V5.2: Generate or Update Compositions

Based on the edit plan from V3, either:

**A) Use existing compositions** (CaptionedClip, FullEdit) with updated props — simplest path for standard edits.

**B) Generate custom composition code** — for non-standard edits (multi-clip compilations, custom animations, unique layouts). Claude writes new TSX files in `video/src/compositions/` using the Remotion skill rules.

Save the composition specification to `projects/[project-name]/4_video/compositions.md`:

```markdown
## Composition Spec

**Composition ID:** [FullEdit / CaptionedClip / Custom]
**Props:**
- videoSrc: "video.mp4"
- captionsSrc: "captions.json"
- highlightColor: "#39E508"
- showIntro: true
- ...

**Custom Code:** [path to custom TSX if generated, or "using default"]
```

#### V5.3: Preview

Start Remotion Studio for the user to preview:

```bash
cd video && npm run studio
```

Present the preview URL (typically `http://localhost:3000`) and tell the user which composition to select.

#### V5.4: Render

On user approval:

```bash
cd video && npx remotion render [CompositionId] out/[project-name].mp4
```

Copy the rendered output:

```bash
cp video/out/[project-name].mp4 [project-path]/4_video/rendered/FINAL_[project-name].mp4
```

#### V5.5: Clean Up

Remove temporary files from `video/public/` (the source video, captions, logo copies).

---

### STEP V6: REVIEW (Iterate)

**Goal:** User reviews the rendered video and provides feedback for iteration.

#### V6.1: Present Output

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VIDEO RENDERED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Output: [project-path]/4_video/rendered/FINAL_[name].mp4
Duration: [X seconds]
Resolution: [WxH]

How does it look? Feedback options:
→ "Looks good" — Ship it
→ Specific feedback — e.g., "captions are too small" / "trim the first 3 seconds" / "change highlight color to yellow"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

#### V6.2: Iterate

If the user has feedback:
1. Update the edit plan or composition props based on feedback
2. Re-render
3. Present again

Maximum 3 revision cycles. If still not right after 3, ask the user if they want to continue or adjust the approach.

#### V6.3: Final Output

When approved, confirm the final file location:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VIDEO APPROVED

Video: [project-path]/4_video/rendered/FINAL_[name].mp4
[If written content was created:]
Written: [project-path]/3_written/FINAL_[type].md

Want me to learn from this project? (y/n)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Format Specification

### Caption Styles

**TikTok Word-Highlight (default):**
- Words appear in groups of 3-5
- Current word highlighted in accent color
- Bold white text with drop shadow
- Positioned in bottom 15% of frame
- Font size: 70px (vertical), 50px (horizontal)

**Lower-Third:**
- Full sentence at bottom of frame
- Semi-transparent background bar
- Positioned at bottom 10%
- Smaller font, more words visible at once

**Centered Block:**
- Words centered in middle of frame
- Larger font, fewer words per group
- Works well for quote-style moments

### Transition Types

| Transition | When to Use |
|-----------|-------------|
| **Fade** (default) | Intro/outro, between segments, most versatile |
| **Cut** | Fast-paced content, between closely related segments |
| **Slide** | Switching topics, before/after comparisons |

### Intro/Outro Templates

**Standard:** Logo fade in → Title text → Fade to content. 2-3 seconds.
**Minimal:** Text card only, no logo. 1-2 seconds.
**None:** Jump straight into content. Best for raw, authentic feel.

---

## Voice & Tone (for Written Content in V4)

Written content produced during V4 should follow the specific content type's voice rules (e.g., `linkedin-post.md`, `x-thread.md`). The video pipeline itself has no voice — it's visual.

---

## Council Adaptations

**Skip the Writer's Council for video.** Video editing is visual and subjective — a 6-person review council doesn't map well to visual media.

Instead, use direct user feedback in V6 with a simple iteration loop: preview → feedback → adjust → re-render.

If written content is produced in V4, that content CAN optionally go through the standard Writer's Council via the normal content type pipeline.

---

## Revision Notes

- **Preview before rendering.** Remotion Studio gives real-time preview at localhost:3000. Always have the user preview before committing to a full render — rendering takes time.
- **Caption timing is everything.** If captions feel off, adjust `combineTokensWithinMilliseconds` in the Captions component. Lower = more frequent word changes (faster feel). Higher = more words per group (calmer feel).
- **Keep intros short.** 2-3 seconds max. Viewers on social media skip anything longer.
- **Default to vertical (9:16)** unless the user specifies otherwise. Most short-form video consumption is vertical.
- **Brand consistency.** Use the same highlight color, fonts, and logo across all video clips. These should be configured in `config.md` during setup.
- **Don't over-edit.** The goal is professional polish (captions, branding), not heavy effects. The content should feel authentic, not produced.

---

## Prerequisites

Before first use, run the video setup script:

```bash
bash scripts/setup-video.sh
```

This installs Remotion dependencies and downloads the Whisper transcription model (~1.5GB one-time download).

**Requirements:**
- Node.js 18+
- ffmpeg (for audio extraction)
- ~2GB disk space (Whisper model + node_modules)

---

*This content type spec is self-contained. It defines the full video clip pipeline, format specification, and revision guidance. The Remotion skills in `.agents/skills/` provide Claude with the domain knowledge needed to write and modify compositions.*
