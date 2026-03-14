"""
LESSON 2: Tool Use — Giving the Agent Abilities
================================================
An agent without tools is just a chatbot. Tools are what let it ACT in the world.

KEY CONCEPT: Tool Design
-------------------------
When you design tools for an agent, you're designing its "action space" —
the set of all things it CAN do. This is one of the most important decisions
in building an agent. Too few tools = limited. Too many tools = confused.

Good tool design follows these principles:
  1. Clear names — Claude picks tools by name. "save_note" > "process_data_v2"
  2. Clear descriptions — Tell Claude WHEN to use it, not just what it does
  3. Minimal parameters — Only require what's truly needed
  4. Useful return values — Return info Claude can reason about

This file separates tools from the agent loop (agent.py) because
good architecture = separation of concerns. The agent loop doesn't
care HOW tools work, just that they exist and return results.
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Where we store persistent data (notes, tasks, etc.)
DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)


# ─────────────────────────────────────────────
# TOOL DEFINITIONS (what Claude sees)
# ─────────────────────────────────────────────
# These are JSON Schema descriptions. Claude reads these to understand:
#   - What tools are available
#   - What each tool does (description)
#   - What inputs each tool needs (properties)
#   - Which inputs are required vs optional
#
# PRO TIP: The description field is the most important part.
# Claude uses it to decide WHEN to call the tool.
# "Save a note for later retrieval" is better than "Writes to a file"
# because it tells Claude the PURPOSE, not the implementation.

TOOL_DEFINITIONS = [
    {
        "name": "get_current_time",
        "description": "Get the current date and time. Use this when the user asks about the current time or date, or when you need to timestamp something.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "save_note",
        "description": "Save a note with a title and content. Use this when the user wants to remember something, jot down an idea, or store information for later.",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "Short title for the note (used as filename)",
                },
                "content": {
                    "type": "string",
                    "description": "The note content",
                },
            },
            "required": ["title", "content"],
        },
    },
    {
        "name": "read_note",
        "description": "Read a previously saved note by its title. Use this when the user asks about something they previously saved.",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "The title of the note to read",
                },
            },
            "required": ["title"],
        },
    },
    {
        "name": "list_notes",
        "description": "List all saved notes. Use this when the user wants to see what notes they have, or when you need to find a specific note.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "add_task",
        "description": "Add a task to the to-do list. Use this when the user wants to track something they need to do.",
        "input_schema": {
            "type": "object",
            "properties": {
                "task": {
                    "type": "string",
                    "description": "Description of the task",
                },
                "priority": {
                    "type": "string",
                    "enum": ["high", "medium", "low"],
                    "description": "Priority level (defaults to medium)",
                },
            },
            "required": ["task"],
        },
    },
    {
        "name": "list_tasks",
        "description": "List all tasks on the to-do list. Use this when the user wants to see their tasks or when you need to check what's pending.",
        "input_schema": {
            "type": "object",
            "properties": {
                "show_completed": {
                    "type": "boolean",
                    "description": "Whether to include completed tasks (default: false)",
                },
            },
            "required": [],
        },
    },
    {
        "name": "complete_task",
        "description": "Mark a task as completed by its number. Use this when the user says they finished a task.",
        "input_schema": {
            "type": "object",
            "properties": {
                "task_number": {
                    "type": "integer",
                    "description": "The task number to mark as complete (1-based)",
                },
            },
            "required": ["task_number"],
        },
    },
    {
        "name": "read_file",
        "description": "Read the contents of a file on the local filesystem. Use this when the user asks you to look at a file.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "The file path to read",
                },
            },
            "required": ["path"],
        },
    },
    {
        "name": "write_file",
        "description": "Write content to a file on the local filesystem. Use this when the user asks you to create or update a file.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "The file path to write to",
                },
                "content": {
                    "type": "string",
                    "description": "The content to write",
                },
            },
            "required": ["path", "content"],
        },
    },
]


# ─────────────────────────────────────────────
# TOOL IMPLEMENTATIONS (what actually happens)
# ─────────────────────────────────────────────
# Each function below is the "real world" side of a tool.
# Claude decides to call "save_note" → we execute save_note() → return result.
#
# Notice: every function returns a STRING. That's important.
# The result goes back into Claude's message history as text,
# so it needs to be human-readable.


def get_current_time(**kwargs) -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S (%A)")


def save_note(title: str, content: str, **kwargs) -> str:
    """Save a note as a JSON file."""
    notes_dir = DATA_DIR / "notes"
    notes_dir.mkdir(exist_ok=True)

    # Sanitize the title for use as filename
    safe_title = "".join(c if c.isalnum() or c in " -_" else "" for c in title)
    safe_title = safe_title.strip().replace(" ", "_").lower()

    note = {
        "title": title,
        "content": content,
        "created_at": datetime.now().isoformat(),
    }

    filepath = notes_dir / f"{safe_title}.json"
    filepath.write_text(json.dumps(note, indent=2))

    return f"Note '{title}' saved successfully."


def read_note(title: str, **kwargs) -> str:
    """Read a note by title."""
    notes_dir = DATA_DIR / "notes"
    if not notes_dir.exists():
        return "No notes found. You haven't saved any notes yet."

    # Try exact match first, then fuzzy
    safe_title = "".join(c if c.isalnum() or c in " -_" else "" for c in title)
    safe_title = safe_title.strip().replace(" ", "_").lower()

    filepath = notes_dir / f"{safe_title}.json"
    if filepath.exists():
        note = json.loads(filepath.read_text())
        return f"Title: {note['title']}\nCreated: {note['created_at']}\n\n{note['content']}"

    # Try partial match
    for f in notes_dir.glob("*.json"):
        if safe_title in f.stem:
            note = json.loads(f.read_text())
            return f"Title: {note['title']}\nCreated: {note['created_at']}\n\n{note['content']}"

    return f"Note '{title}' not found. Use list_notes to see available notes."


def list_notes(**kwargs) -> str:
    """List all saved notes."""
    notes_dir = DATA_DIR / "notes"
    if not notes_dir.exists():
        return "No notes found."

    notes = []
    for f in sorted(notes_dir.glob("*.json")):
        note = json.loads(f.read_text())
        notes.append(f"  - {note['title']} (saved {note['created_at'][:10]})")

    if not notes:
        return "No notes found."

    return "Your notes:\n" + "\n".join(notes)


def _load_tasks() -> list:
    """Load tasks from disk."""
    tasks_file = DATA_DIR / "tasks.json"
    if tasks_file.exists():
        return json.loads(tasks_file.read_text())
    return []


def _save_tasks(tasks: list):
    """Save tasks to disk."""
    tasks_file = DATA_DIR / "tasks.json"
    tasks_file.write_text(json.dumps(tasks, indent=2))


def add_task(task: str, priority: str = "medium", **kwargs) -> str:
    """Add a task to the to-do list."""
    tasks = _load_tasks()
    tasks.append({
        "task": task,
        "priority": priority,
        "completed": False,
        "created_at": datetime.now().isoformat(),
    })
    _save_tasks(tasks)
    return f"Task added: '{task}' (priority: {priority})"


def list_tasks(show_completed: bool = False, **kwargs) -> str:
    """List all tasks."""
    tasks = _load_tasks()
    if not tasks:
        return "No tasks found. Your to-do list is empty."

    lines = []
    for i, t in enumerate(tasks, 1):
        if t["completed"] and not show_completed:
            continue
        status = "✅" if t["completed"] else "⬜"
        pri = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(t["priority"], "")
        lines.append(f"  {i}. {status} {pri} {t['task']}")

    if not lines:
        return "All tasks completed! 🎉"

    return "Your tasks:\n" + "\n".join(lines)


def complete_task(task_number: int, **kwargs) -> str:
    """Mark a task as complete."""
    tasks = _load_tasks()
    if task_number < 1 or task_number > len(tasks):
        return f"Invalid task number. You have {len(tasks)} tasks."

    tasks[task_number - 1]["completed"] = True
    _save_tasks(tasks)
    return f"Task '{tasks[task_number - 1]['task']}' marked as complete! ✅"


def read_file(path: str, **kwargs) -> str:
    """Read a file from disk."""
    try:
        p = Path(path).expanduser()
        if not p.exists():
            return f"File not found: {path}"
        if p.stat().st_size > 100_000:
            return f"File too large ({p.stat().st_size} bytes). Max 100KB."
        return p.read_text()
    except Exception as e:
        return f"Error reading file: {e}"


def write_file(path: str, content: str, **kwargs) -> str:
    """Write content to a file."""
    try:
        p = Path(path).expanduser()
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)
        return f"File written: {path} ({len(content)} chars)"
    except Exception as e:
        return f"Error writing file: {e}"


# ─────────────────────────────────────────────
# TOOL ROUTER
# ─────────────────────────────────────────────
# This maps tool names to their implementations.
# When Claude says "call save_note", we look it up here.
#
# This is a simple dict-based router. In production systems,
# you might use decorators, a registry pattern, or even
# dynamically loaded plugins. But a dict works great.

TOOL_FUNCTIONS = {
    "get_current_time": get_current_time,
    "save_note": save_note,
    "read_note": read_note,
    "list_notes": list_notes,
    "add_task": add_task,
    "list_tasks": list_tasks,
    "complete_task": complete_task,
    "read_file": read_file,
    "write_file": write_file,
}


def execute_tool(name: str, tool_input: dict) -> str:
    """Execute a tool by name. Returns the result as a string.

    This is the single entry point the agent loop uses.
    It doesn't need to know how any specific tool works —
    it just passes the name and input, gets a string back.
    """
    func = TOOL_FUNCTIONS.get(name)
    if func is None:
        return f"Error: Unknown tool '{name}'. Available tools: {list(TOOL_FUNCTIONS.keys())}"

    try:
        return func(**tool_input)
    except Exception as e:
        # Return the error as a string — don't crash the agent!
        # Claude will see this error and can adjust its approach.
        return f"Error executing {name}: {e}"
