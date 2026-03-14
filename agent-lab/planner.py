"""
LESSON 4: Multi-Step Planning
==============================

THE PLANNING PROBLEM:
  Simple agents are reactive — they respond to each message independently.
  But real tasks often require multiple steps:
    "Summarize my notes and create tasks for anything unfinished"
    → 1. List all notes
    → 2. Read each one
    → 3. Identify unfinished items
    → 4. Create tasks for each

  Without planning, the agent just wings it. Sometimes it works.
  Sometimes it forgets steps or goes in circles.

THE SOLUTION:
  Give the agent a "plan" tool. Before acting, it writes down its plan.
  Then it executes each step and tracks progress.

WHY THIS MATTERS:
  Planning is what separates "agents" from "chatbots with tools."
  A chatbot answers questions. An agent achieves goals.

  Plans also help with:
    - Transparency: the user can SEE what the agent intends to do
    - Debugging: when something goes wrong, you can see WHERE it went wrong
    - Recovery: if a step fails, the agent knows what it already completed

DESIGN NOTES:
  We're adding TWO tools:
    1. make_plan — Claude creates a step-by-step plan
    2. update_plan — Claude marks steps as done or adjusts the plan

  The plan lives in memory during the conversation. We don't persist it
  because plans are task-specific, not knowledge.
"""

import json

# In-memory plan storage (per session)
_current_plan = {"goal": "", "steps": [], "status": "no_plan"}


def make_plan(goal: str, steps: list, **kwargs) -> str:
    """Create a multi-step plan to achieve a goal.

    Claude calls this when it recognizes a task needs multiple steps.
    The plan is stored in memory and displayed to the user.
    """
    global _current_plan

    _current_plan = {
        "goal": goal,
        "steps": [
            {"description": step, "status": "pending"}
            for step in steps
        ],
        "status": "in_progress",
    }

    lines = [f"Plan created: {goal}"]
    for i, step in enumerate(steps, 1):
        lines.append(f"  {i}. ⬜ {step}")

    return "\n".join(lines)


def update_plan(step_number: int, status: str, note: str = "", **kwargs) -> str:
    """Update the status of a plan step.

    Claude calls this after completing (or failing) each step.
    This keeps the plan in sync with reality.
    """
    global _current_plan

    if _current_plan["status"] == "no_plan":
        return "No active plan. Use make_plan first."

    if step_number < 1 or step_number > len(_current_plan["steps"]):
        return f"Invalid step number. Plan has {len(_current_plan['steps'])} steps."

    step = _current_plan["steps"][step_number - 1]
    step["status"] = status
    if note:
        step["note"] = note

    # Check if all steps are done
    all_done = all(s["status"] in ("done", "skipped") for s in _current_plan["steps"])
    if all_done:
        _current_plan["status"] = "completed"

    # Format current plan status
    status_icons = {"pending": "⬜", "in_progress": "🔄", "done": "✅", "failed": "❌", "skipped": "⏭️"}
    lines = [f"Plan: {_current_plan['goal']} ({'COMPLETE' if all_done else 'in progress'})"]
    for i, s in enumerate(_current_plan["steps"], 1):
        icon = status_icons.get(s["status"], "?")
        line = f"  {i}. {icon} {s['description']}"
        if s.get("note"):
            line += f" — {s['note']}"
        lines.append(line)

    return "\n".join(lines)


# ─────────────────────────────────────────────
# TOOL DEFINITIONS
# ─────────────────────────────────────────────

PLANNER_TOOL_DEFINITIONS = [
    {
        "name": "make_plan",
        "description": "Create a step-by-step plan to accomplish a complex goal. Use this BEFORE starting any task that requires 3+ steps. Break the goal into concrete, actionable steps.",
        "input_schema": {
            "type": "object",
            "properties": {
                "goal": {
                    "type": "string",
                    "description": "The overall goal to accomplish",
                },
                "steps": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Ordered list of steps to achieve the goal",
                },
            },
            "required": ["goal", "steps"],
        },
    },
    {
        "name": "update_plan",
        "description": "Update the status of a step in the current plan. Call this after completing each step to track progress.",
        "input_schema": {
            "type": "object",
            "properties": {
                "step_number": {
                    "type": "integer",
                    "description": "Which step to update (1-based)",
                },
                "status": {
                    "type": "string",
                    "enum": ["in_progress", "done", "failed", "skipped"],
                    "description": "New status for the step",
                },
                "note": {
                    "type": "string",
                    "description": "Optional note about what happened",
                },
            },
            "required": ["step_number", "status"],
        },
    },
]

PLANNER_TOOL_FUNCTIONS = {
    "make_plan": make_plan,
    "update_plan": update_plan,
}
