# The Productivity Coach

A Claude Code skill that acts as your personal productivity coach — plan your days, break down big projects, prioritize ruthlessly, time-block your calendar, and stay focused on what actually matters.

```
┌──────────────────────────────────────────────────────────────────────┐
│                       THE PRODUCTIVITY COACH                         │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  --plan               → Full daily planning session                  │
│  --breakdown [project]→ Decompose a big project into action items    │
│  --prioritize         → Ruthless priority sort on your current list  │
│  --schedule           → Time-block your day on a calendar            │
│  --focus              → Start a focus session on your #1 priority    │
│  --review             → End-of-day review & tomorrow prep            │
│  --weekly             → Weekly review & planning                     │
│  --status             → Quick view of today's plan & progress        │
│  --configure          → Set up your work preferences                 │
│                                                                      │
│  ─── THE DAILY LOOP ───                                              │
│                                                                      │
│  Morning:   --plan                                                   │
│  Anytime:   --breakdown, --prioritize, --focus                       │
│  Evening:   --review                                                 │
│  Friday:    --weekly                                                 │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

---

## Quick Start

1. Run `/productivity-coach --configure` to set up your work hours, energy patterns, and current projects.
2. Each morning, run `/productivity-coach --plan` to plan your day.
3. Use `/productivity-coach --focus` to lock in on your top priority.
4. End the day with `/productivity-coach --review`.

## What It Does

### Daily Planning
Brain dump everything on your mind. The coach captures it, prioritizes ruthlessly (max 3 P1s — no exceptions), time-blocks your calendar around meetings and energy levels, and gives you a clear plan with one #1 priority.

### Project Breakdowns
Hand it a big, overwhelming project. It defines what "done" looks like, breaks it into milestones, decomposes milestones into concrete action items (every task passes the "sit down and start" test), identifies the critical path, and gives you the one next action.

### Priority Management
The coach runs every task through impact, urgency, dependency, and leverage filters. It pushes back when you have too many "priorities" and forces clarity. If everything is P1, nothing is P1.

### Calendar Time Blocking
Builds a real schedule grounded in your available hours. P1 tasks go in peak energy slots. Breaks every 90 minutes. 20% buffer for interruptions. If your tasks exceed available time, it tells you what to cut.

### Focus Sessions
Locks you in on one task with specific steps. If you get distracted, it calls it out. If you're stuck, it helps find the smallest next step. No multitasking allowed.

### Reviews
End-of-day reviews compare plan vs reality. Weekly reviews surface patterns, completion rates, and help plan the next week around 3 key outcomes.

## File Structure

```
├── .claude/commands/
│   └── productivity-coach.md    ← The skill
├── templates/
│   ├── daily-plan.md            ← Daily plan template
│   ├── project-breakdown.md     ← Project decomposition template
│   ├── weekly-review.md         ← Weekly review template
│   └── config.example.md        ← Example configuration
├── plans/                       ← Your data (gitignored)
│   ├── daily/                   ← Plans by date
│   ├── projects/                ← Project breakdowns
│   └── reviews/                 ← Weekly reviews
└── config.md                    ← Your preferences (gitignored)
```

## Philosophy

- **Ruthless prioritization** — Only 1-3 things matter today. Everything else is noise.
- **Time is finite** — Every plan fits real hours. No fantasy schedules.
- **Energy matching** — Hard work during peak hours. Admin during low energy.
- **Action-level specificity** — If you can't start it in 30 seconds, it's not a task.
- **Momentum over perfection** — Done beats perfect. Shipped beats polished.
