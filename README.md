# The Content Machine

A complete content creation system built as a Claude Code skill. Takes you from blank page to publish-ready content through a 6-step process.

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

## The Teams

### The Interview Panel (Steps 1-2)

| Interviewer | Style | Superpower |
|-------------|-------|------------|
| **Tim Ferriss** | Tactical deconstruction | Extracts specific processes and frameworks |
| **Joe Rogan** | Follow the curiosity | Pulls out stories through casual conversation |
| **Larry King** | Short, direct questions | Cuts to the core: "Why?" "How did that feel?" |
| **Howard Stern** | Disarmingly personal | Gets you to reveal what you normally wouldn't |
| **Michael Barbaro** | Narrative clarity | "Help me understand..." Makes complex ideas accessible |
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

## Installation

Clone this repo and use it as your content working directory:

```bash
git clone https://github.com/[your-username]/content-machine.git
cd content-machine
```

Or copy the skill into your existing Claude Code skills:

```bash
cp SKILL.md ~/.claude/skills/content-machine/SKILL.md
```

---

## Usage

### Full Pipeline (Steps 1-6)

```
/content-machine --full [topic]
/content-machine --full (no topic - panel helps you find one)
```

### Create New Project

```
/content-machine --new my-project-name
```

### Interview Only (Steps 1-4)

```
/content-machine --interview [topic]
```

### Council Review (Steps 5-6)

```
/content-machine [paste your content]
```

### Revision Loop (Step 6)

```
/content-machine --revise [paste your content]
```

---

## Folder Structure

```
/content-machine/
├── SKILL.md              ← The process definition
├── style-guide.md        ← Your writing voice
├── README.md             ← You are here
├── projects/
│   └── [project-name]/
│       ├── 1_input/      ← Topic selection
│       ├── 2_interview/  ← Interview transcript
│       ├── 3_production/ ← Raw .md file (source of truth)
│       ├── 4_refinement/ ← Platform drafts
│       ├── 5_editing/    ← Council review
│       └── 6_final/      ← Approved versions
└── archive/              ← Completed projects
```

---

## The 6 Steps

### Step 1: INPUT
The Interview Panel suggests 5-6 compelling topics based on your unique experiences. You pick one.

### Step 2: INTERVIEW
One question at a time. Each interviewer reads your previous response and builds on it. The panel pushes for specificity—no vague answers allowed.

### Step 3: PRODUCTION
Your interview becomes a raw .md file that preserves your exact words. This is the source of truth for all content.

### Step 4: REFINEMENT
Select platforms (Newsletter, LinkedIn, X/Twitter, etc.). The system drafts each piece using your style guide.

### Step 5: EDITING
All 6 council members review and score your content. Priority fixes are ranked.

### Step 6: REVISION LOOP
Revise based on feedback, gather additional context if needed, and re-score until 9/10.

---

## Pro Tips

1. **The raw file is sacred.** Don't paraphrase away your actual words.
2. **Style guide is mandatory.** Your voice, not generic "good writing."
3. **Hook first.** If Shaan fails it, nothing else matters.
4. **9/10 is the bar.** Don't ship until the council agrees it's ready.

---

## Credits

Built by [Alex Lieberman](https://twitter.com/businessbarista)

Based on the styles and frameworks of:
- Morgan Housel (The Psychology of Money)
- Tim Urban (Wait But Why)
- Shaan Puri (My First Million)
- Greg Isenberg (Late Checkout)
- David Perell (Write of Passage)

## License

MIT - Use it, share it, make it better.
