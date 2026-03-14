"""
LESSON 3: Memory — Making the Agent Remember Across Sessions
=============================================================

THE MEMORY PROBLEM:
  When you close the agent and reopen it, all conversation history is gone.
  The agent doesn't know your name, your preferences, or what you talked about.

  This is the #1 thing that separates a toy agent from a useful one.

THE SOLUTION:
  We create a persistent memory layer — a simple file-based store that the
  agent can write to and read from across sessions.

TYPES OF MEMORY IN AGENTIC SYSTEMS:
  1. Short-term (conversation buffer)  → the messages list
  2. Long-term (persistent facts)      → what we're building here
  3. Episodic (past conversations)     → summaries of previous sessions
  4. Semantic (knowledge graph)         → structured relationships (advanced)

  We're implementing #2 (long-term memory) and #3 (episodic memory).
  These two give you 90% of the value. #4 is rarely worth the complexity.

DESIGN DECISIONS:
  - JSON files, not a database. Why? Simplicity. You can open and read them.
    A database adds complexity without value until you have thousands of memories.
  - Memories are tagged with categories for retrieval.
  - Each memory has a timestamp so old ones can be pruned.
  - We inject memories into the system prompt, not into messages.
    This keeps them "always on" without polluting conversation history.
"""

import json
from datetime import datetime
from pathlib import Path


DATA_DIR = Path(__file__).parent / "data"
MEMORIES_FILE = DATA_DIR / "memories.json"
SESSIONS_DIR = DATA_DIR / "sessions"


def _load_memories() -> list:
    """Load all memories from disk."""
    if MEMORIES_FILE.exists():
        return json.loads(MEMORIES_FILE.read_text())
    return []


def _save_memories(memories: list):
    """Save memories to disk."""
    DATA_DIR.mkdir(exist_ok=True)
    MEMORIES_FILE.write_text(json.dumps(memories, indent=2))


# ─────────────────────────────────────────────
# MEMORY TOOLS (Claude can call these)
# ─────────────────────────────────────────────

def save_memory(fact: str, category: str = "general", **kwargs) -> str:
    """Save an important fact to long-term memory.

    This is the tool Claude calls when it learns something worth remembering.
    For example: the user's name, their preferences, important dates, etc.
    """
    memories = _load_memories()

    # Don't save duplicates
    for m in memories:
        if m["fact"].lower() == fact.lower():
            return f"Already remembered: '{fact}'"

    memories.append({
        "fact": fact,
        "category": category,
        "created_at": datetime.now().isoformat(),
    })

    _save_memories(memories)
    return f"Remembered: '{fact}' (category: {category})"


def recall_memories(query: str = "", category: str = "", **kwargs) -> str:
    """Search memories by keyword or category.

    Claude calls this when it needs to look something up about the user.
    Simple keyword search — good enough for hundreds of memories.
    For thousands, you'd want embeddings + vector search.
    """
    memories = _load_memories()
    if not memories:
        return "No memories stored yet."

    results = memories

    # Filter by category if provided
    if category:
        results = [m for m in results if m["category"] == category]

    # Filter by keyword if provided
    if query:
        query_lower = query.lower()
        results = [m for m in results if query_lower in m["fact"].lower()]

    if not results:
        return f"No memories found matching query='{query}' category='{category}'"

    lines = []
    for m in results:
        lines.append(f"  - [{m['category']}] {m['fact']}")

    return "Recalled memories:\n" + "\n".join(lines)


def list_all_memories(**kwargs) -> str:
    """List all stored memories, grouped by category."""
    memories = _load_memories()
    if not memories:
        return "No memories stored yet."

    # Group by category
    by_category = {}
    for m in memories:
        cat = m["category"]
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(m["fact"])

    lines = []
    for cat, facts in sorted(by_category.items()):
        lines.append(f"\n  [{cat}]")
        for fact in facts:
            lines.append(f"    - {fact}")

    return "All memories:" + "\n".join(lines)


# ─────────────────────────────────────────────
# MEMORY TOOL DEFINITIONS (for Claude to see)
# ─────────────────────────────────────────────

MEMORY_TOOL_DEFINITIONS = [
    {
        "name": "save_memory",
        "description": "Save an important fact about the user to long-term memory. Use this when you learn something worth remembering: their name, preferences, important dates, key context. This persists across sessions.",
        "input_schema": {
            "type": "object",
            "properties": {
                "fact": {
                    "type": "string",
                    "description": "The fact to remember (e.g., 'User's name is Alex')",
                },
                "category": {
                    "type": "string",
                    "enum": ["personal", "preference", "project", "general"],
                    "description": "Category for organization (default: general)",
                },
            },
            "required": ["fact"],
        },
    },
    {
        "name": "recall_memories",
        "description": "Search your long-term memory for facts about the user. Use this when the user references something from a previous conversation, or when you need context about them.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Keyword to search for in memories",
                },
                "category": {
                    "type": "string",
                    "enum": ["personal", "preference", "project", "general"],
                    "description": "Optionally filter by category",
                },
            },
            "required": [],
        },
    },
    {
        "name": "list_all_memories",
        "description": "List everything you remember about the user, grouped by category. Use when the user asks 'what do you know about me?' or similar.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
]

MEMORY_TOOL_FUNCTIONS = {
    "save_memory": save_memory,
    "recall_memories": recall_memories,
    "list_all_memories": list_all_memories,
}


# ─────────────────────────────────────────────
# SESSION MEMORY (Episodic Memory)
# ─────────────────────────────────────────────
# At the end of each conversation, we save a summary.
# Next time the agent starts, it can review past sessions
# for context. This is "episodic memory" — remembering
# WHAT HAPPENED, not just facts.

def save_session_summary(messages: list, summary: str = ""):
    """Save a summary of the current conversation session.

    Called when the user exits. In a production system,
    you'd have Claude generate the summary automatically.
    Here we save the raw message count + any provided summary.
    """
    SESSIONS_DIR.mkdir(parents=True, exist_ok=True)

    session = {
        "timestamp": datetime.now().isoformat(),
        "message_count": len(messages),
        "summary": summary or f"Session with {len(messages)} messages",
    }

    # Use timestamp as filename
    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    (SESSIONS_DIR / filename).write_text(json.dumps(session, indent=2))


def get_recent_sessions(limit: int = 3) -> str:
    """Get summaries of recent sessions for context.

    This is injected into the system prompt so Claude knows
    what happened in previous conversations.
    """
    if not SESSIONS_DIR.exists():
        return ""

    sessions = sorted(SESSIONS_DIR.glob("*.json"), reverse=True)[:limit]
    if not sessions:
        return ""

    lines = ["Recent sessions:"]
    for s in sessions:
        data = json.loads(s.read_text())
        lines.append(f"  - {data['timestamp'][:16]}: {data['summary']}")

    return "\n".join(lines)


# ─────────────────────────────────────────────
# CONTEXT BUILDER
# ─────────────────────────────────────────────
# This builds the "memory context" that gets injected into
# the system prompt. It gives Claude awareness of:
#   1. What it knows about the user (long-term memory)
#   2. What happened in recent sessions (episodic memory)
#
# This is the KEY PATTERN: memory → system prompt injection.
# It's simple, effective, and how most production agents work.

def build_memory_context() -> str:
    """Build a context string from memories and recent sessions.

    This goes into the system prompt so Claude always has context.
    """
    parts = []

    # Long-term memories
    memories = _load_memories()
    if memories:
        parts.append("Things you remember about this user:")
        for m in memories:
            parts.append(f"  - [{m['category']}] {m['fact']}")

    # Recent sessions
    sessions_context = get_recent_sessions()
    if sessions_context:
        parts.append("")
        parts.append(sessions_context)

    if not parts:
        return "This is a new user. You don't have any memories yet. Pay attention to details worth remembering."

    return "\n".join(parts)
