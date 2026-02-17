# The Content Machine

A complete content creation system built as a Claude Code skill. Takes you from blank page to publish-ready content through a structured pipeline — The Oracle finds your topic, the Interview Panel extracts your stories, and the Writer's Council refines until it's a 9/10.

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

---

## Content Types

Content types are modular specs in the `content-types/` directory. Each defines its own format, voice adaptation, and pipeline.

| Content Type | File | Pipeline | Description |
|-------------|------|----------|-------------|
| Long Post | `content-types/long-post.md` | Standard | Story-driven long-form (1,000-2,500 words) |
| LinkedIn Post | `content-types/linkedin-post.md` | Standard | Professional-casual with pattern-interrupt hook (3,000 char max) |
| X Thread | `content-types/x-thread.md` | Standard | Punchy, hook-heavy thread (10-15 tweets) |
| Playbook | `content-types/playbook.md` | Custom (P1-P5) | Expert playbook from YouTube interviews (2,500-4,000 words) |

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
│   └── playbook.md                ← Playbook pipeline + format spec
├── scripts/
│   ├── fetch-transcript.sh        ← YouTube transcript fetcher
│   └── daily-oracle.sh            ← Automated daily Oracle scanner
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
