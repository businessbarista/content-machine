# The Content Machine

A complete content creation system built as a Claude Code skill. Takes you from blank page to publish-ready content — written and video — through a structured pipeline. The Oracle finds your topic, the Interview Panel extracts your stories, and the Writer's Council refines until it's a 9/10. Upload a short-form video and get both an edited clip (with captions, branding, transitions) and written posts.

**Each person writes in their own voice.** You create a personal style guide during setup, and the system applies it to every draft.

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
│  Content types are modular — each type (long post, LinkedIn,        │
│  X thread, playbook, etc.) has its own spec in content-types/.      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/[your-username]/content-machine.git
cd content-machine
```

### 2. Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI installed
- (Optional) Slack MCP server — for The Oracle to scan your Slack
- (Optional) Notion MCP server — for The Oracle to scan your Notion
- (For video editing) Node.js 18+ and ffmpeg — run `bash scripts/setup-video.sh` after cloning

### 3. Run setup

```
/content-machine --setup
```

This walks you through:
- **Creating your style guide** — analyze your best posts, answer interview questions, or start blank
- **Connecting apps** — Slack User ID, Oracle channel, Notion
- **Reviewing content types** — see what's available, customize or add your own

### 4. Create your first piece

```
/content-machine --full [topic]
```

Or let The Oracle find a topic for you:

```
/content-machine --oracle
```

---

## Commands

| Command | What It Does |
|---------|-------------|
| `/content-machine --setup` | First-time setup (style guide, apps, content types) |
| `/content-machine --full [topic]` | Full pipeline: Oracle → Interview → Draft → Council → 9/10 |
| `/content-machine --new [name]` | Create a new project folder |
| `/content-machine --oracle` | Run The Oracle only (find content spikes) |
| `/content-machine --interview [topic]` | Start from the interview step |
| `/content-machine [content]` | Send content directly to the Writer's Council |
| `/content-machine --revise [content]` | Revision loop only |
| `/content-machine --reviewer [name] [content]` | Single reviewer (morgan, shaan, slop, etc.) |
| `/content-machine --learn [project]` | Learn from a project's revision history |
| `/content-machine --learn --verbal "feedback"` | Learn from direct feedback |

### Content Type Shortcuts

| Command | Content Type |
|---------|-------------|
| `/content-machine --long-post [topic]` | Long-form post (1,000-2,500 words) |
| `/content-machine --linkedin [topic]` | LinkedIn post (3,000 char max) |
| `/content-machine --x-thread [topic]` | X/Twitter thread (10-15 tweets) |
| `/content-machine --playbook [YouTube URL]` | Playbook from YouTube interview |
| `/content-machine --podcast-promo [YouTube URL]` | Podcast promo post for X & LinkedIn |
| `/content-machine --video-clip [video path]` | Edit video with captions + branding (+ optional written posts) |

---

## Use All of It or Parts of It

The Content Machine is modular — you can run the full pipeline end-to-end, or jump into any step on its own. Use what you need, skip what you don't.

**Full pipeline** — you have no idea what to write about:
```
/content-machine --full
```
Runs Oracle → Interview → Production → Refinement → Council → Revision Loop.

**Skip ideation** — you already have a topic or source material:
```
/content-machine --interview "my take on why most AI implementations fail"
/content-machine --playbook https://youtube.com/watch?v=...
/content-machine --podcast-promo https://youtube.com/watch?v=...
```
Jumps straight to extracting content from your idea or source, skipping the Oracle.

**Skip ideation and extraction** — you already have a draft or raw material:
```
/content-machine --linkedin
```
Then paste your raw notes, transcript, or rough draft. The system refines it into a polished piece using your style guide.

**Editing only** — you have a finished draft and just want feedback:
```
/content-machine [paste your draft]
```
Sends it directly to the Writer's Council for scoring and feedback. No ideation, no extraction, no drafting.

**Single reviewer** — you just want one perspective:
```
/content-machine --reviewer shaan [paste your draft]
/content-machine --reviewer slop [paste your draft]
```

**Revision only** — you have council feedback and want to iterate:
```
/content-machine --revise [paste your draft]
```

**Video editing** — you have a short-form video and want it polished with captions + branding:
```
/content-machine --video-clip path/to/video.mp4
```
Transcribes, adds TikTok-style captions, intro/outro, and renders via Remotion. Add `--with-posts` to also generate written content from the transcript.

**Learning only** — you published something and want the system to learn from your edits:
```
/content-machine --learn [project-name]
/content-machine --learn --verbal "hooks should be shorter"
```

The point: you don't have to use every step every time. The pipeline is a menu, not a checklist.

---

## Content Types

Content types are modular specs in the `content-types/` directory. Each defines its own format, voice adaptation, and pipeline.

| Content Type | File | Pipeline | Description |
|-------------|------|----------|-------------|
| Long Post | `content-types/long-post.md` | Standard | Story-driven long-form (1,000-2,500 words) |
| LinkedIn Post | `content-types/linkedin-post.md` | Standard | Professional-casual with pattern-interrupt hook (3,000 char max) |
| X Thread | `content-types/x-thread.md` | Standard | Punchy, hook-heavy thread (10-15 tweets) |
| Playbook | `content-types/playbook.md` | Custom (P1-P5) | Expert playbook from YouTube interviews (2,500-4,000 words) |
| Podcast Promo | `content-types/podcast-promo.md` | Custom (P1-P5) | Podcast episode promo for X & LinkedIn with standalone tactical value |
| Video Clip | `content-types/video-clip.md` | Custom (V1-V6) | Edit short-form video with captions, branding, transitions + optional written posts |

### Creating Your Own Content Type

Copy the template and fill it in:

```bash
cp content-types/_template.md content-types/my-new-type.md
```

The template defines the standard sections every content type needs:
- **Overview** — command flag, description, length, platform
- **Pipeline** — `standard` (uses Steps 1-6) or `custom` (defines its own pipeline)
- **Format Specification** — structure, voice adaptation, length constraints
- **Drafting Instructions** — what to read and how to write it
- **Council Adaptations** — modifications to the Writer's Council review (if any)

---

## File Structure

```
content-machine/
├── .claude/
│   └── commands/
│       └── content-machine.md     ← Core system (the skill)
├── .agents/
│   └── skills/                    ← Auto-loaded Claude Code skills
│       ├── remotion-best-practices/  ← Video creation rules (30+ rule files)
│       ├── ui-ux-pro-max/            ← Design system (97 colors, 57 fonts, 50+ styles)
│       └── copywriting/              ← Conversion copy principles
├── README.md                      ← You are here
├── config.md                      ← Your settings (gitignored, created during --setup)
├── style-guide.md                 ← Your writing voice (gitignored, created during --setup)
├── style-guide.example.md         ← Example of a completed style guide
├── content-lessons.md             ← Lessons learned from your feedback
├── content-types/
│   ├── _template.md               ← Template for creating new content types
│   ├── long-post.md               ← Long-form post spec
│   ├── linkedin-post.md           ← LinkedIn post spec
│   ├── x-thread.md                ← X/Twitter thread spec
│   ├── playbook.md                ← Playbook pipeline + format spec
│   ├── podcast-promo.md           ← Podcast promo for X & LinkedIn
│   └── video-clip.md              ← Video editing pipeline + format spec
├── video/                         ← Remotion project for video editing
│   ├── package.json
│   ├── src/                       ← Compositions, components, transcription
│   └── public/                    ← Temp assets during render
├── assets/                        ← Brand assets for video (logos, fonts, images)
├── scripts/
│   ├── fetch-transcript.sh        ← YouTube transcript fetcher
│   ├── daily-oracle.sh            ← Automated daily Oracle scanner
│   └── setup-video.sh             ← One-time video setup (Remotion + Whisper)
├── projects/                      ← Your work (gitignored)
│   └── [project-name]/
│       ├── 1_oracle/
│       ├── 2_interview/
│       ├── 3_production/
│       ├── 4_refinement/
│       ├── 5_editing/
│       └── 6_final/
└── oracle-reports/                ← Oracle output (gitignored)
```

---

## The Teams

### The Oracle (Step 1)

Mines your connected apps for content "spikes" — moments you naturally created something worth sharing.

| Source | What It Finds |
|--------|---------------|
| **Slack** | Strong POVs, rants, teaching moments in DMs and channels |
| **Notion** | Insights, frameworks, lessons buried in your notes |

### The Interview Panel (Step 2)

| Interviewer | Style | Superpower |
|-------------|-------|------------|
| **Tim Ferriss** | Tactical deconstruction | Extracts specific processes and frameworks |
| **Joe Rogan** | Follow the curiosity | Pulls out stories through casual conversation |
| **Larry King** | Short, direct questions | Cuts to the core: "Why?" "How did that feel?" |
| **Howard Stern** | Disarmingly personal | Gets you to reveal what you normally wouldn't |
| **Michael Barbaro** | Narrative clarity | Makes complex ideas accessible |
| **Barbara Walters** | Emotional depth | Finds the human truth that makes content resonate |

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

## The Learning Loop

The system gets smarter over time. After each project, it can compare your edits against the original draft and extract lessons:

```
/content-machine --learn [project-name]
```

Lessons are saved to `content-lessons.md` and applied to every future first draft. The file has a 30-lesson hard cap with periodic review — proven lessons graduate into your style guide.

---

## Pro Tips

1. **The raw file is sacred.** Don't paraphrase away your actual words.
2. **Style guide is mandatory.** Your voice, not generic "good writing."
3. **Hook first.** If Shaan fails it, nothing else matters.
4. **9/10 is the bar.** Don't ship until the council agrees it's ready.
5. **Content types are modular.** Add new ones anytime — just copy the template.

---

## Credits

Built by [Alex Lieberman](https://twitter.com/businessbarista)

Council based on the styles and frameworks of Morgan Housel, Tim Urban, Shaan Puri, Greg Isenberg, and David Perell.

## License

MIT — Use it, share it, make it better.
