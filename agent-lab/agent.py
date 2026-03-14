"""
PERSONAL ASSISTANT AGENT
========================
Lessons 1-5: Agent Loop + Tool Use + Memory + Planning + Error Recovery

A complete agentic system that demonstrates every core pattern:
  - The agent loop (think → act → observe → repeat)
  - Tool use (notes, tasks, files, time)
  - Long-term memory (remembers facts across sessions)
  - Episodic memory (remembers past sessions)
  - Multi-step planning (breaks goals into steps)
  - Error recovery (graceful handling of failures)

Run it:  python agent.py
Requires:  ANTHROPIC_API_KEY environment variable

Architecture:
  agent.py   — The agent loop + conversation management (you are here)
  tools.py   — Task/note/file tools + definitions
  memory.py  — Long-term + episodic memory
  planner.py — Multi-step planning tools
  data/      — Persistent storage (auto-created)

LESSON 5: Error Recovery & Production Patterns
===============================================
A real agent needs to handle failures gracefully:

  1. API errors      → retry with backoff
  2. Tool errors     → return error string, let Claude adapt
  3. Bad tool calls  → validate inputs, return helpful errors
  4. Rate limits     → wait and retry
  5. Context overflow → summarize and continue

We implement #1-4 below. #5 (context management) is an advanced topic
that becomes important with long conversations.
"""

import anthropic
import json
import time
import sys

from tools import TOOL_DEFINITIONS, TOOL_FUNCTIONS
from memory import (
    MEMORY_TOOL_DEFINITIONS,
    MEMORY_TOOL_FUNCTIONS,
    build_memory_context,
    save_session_summary,
)
from planner import PLANNER_TOOL_DEFINITIONS, PLANNER_TOOL_FUNCTIONS

# ─────────────────────────────────────────────
# COMBINE ALL TOOLS (Plugin pattern)
# ─────────────────────────────────────────────
# Each module registers its own tools. We combine them here.
# Adding a new capability = create a module + merge it in.
# This is the simplest form of a plugin architecture.

ALL_TOOL_DEFINITIONS = (
    TOOL_DEFINITIONS
    + MEMORY_TOOL_DEFINITIONS
    + PLANNER_TOOL_DEFINITIONS
)

ALL_TOOL_FUNCTIONS = {
    **TOOL_FUNCTIONS,
    **MEMORY_TOOL_FUNCTIONS,
    **PLANNER_TOOL_FUNCTIONS,
}


def execute_tool(name: str, tool_input: dict) -> str:
    """Execute any registered tool with error handling.

    LESSON 5 CONCEPT: Defensive tool execution.
    We never let a tool crash the agent. Instead, errors become
    strings that Claude can read and reason about.

    This is critical because Claude can RECOVER from errors.
    If save_note fails, Claude might try a different filename.
    If read_file fails, Claude might ask the user for the correct path.
    But if the agent CRASHES, recovery is impossible.
    """
    func = ALL_TOOL_FUNCTIONS.get(name)
    if func is None:
        available = ", ".join(sorted(ALL_TOOL_FUNCTIONS.keys()))
        return f"Error: Unknown tool '{name}'. Available tools: {available}"

    try:
        result = func(**tool_input)
        # Ensure result is a string (defensive programming)
        return str(result) if result is not None else "Done (no output)"
    except TypeError as e:
        # Wrong arguments — give Claude helpful info
        return f"Error: Wrong arguments for {name}: {e}. Check the tool's input_schema."
    except Exception as e:
        return f"Error executing {name}: {type(e).__name__}: {e}"


def call_api_with_retry(client, max_retries: int = 3, **kwargs):
    """Call the Claude API with retry logic for transient errors.

    LESSON 5 CONCEPT: Retry with exponential backoff.

    Not all errors are permanent. Network glitches, rate limits, and
    server blips are TRANSIENT — they'll work if you try again.

    Exponential backoff means: wait 1s, then 2s, then 4s.
    This prevents hammering the API when it's struggling.

    We only retry on specific error types:
      - APIConnectionError  → network issue
      - RateLimitError      → too many requests
      - InternalServerError → server-side issue

    We do NOT retry on:
      - AuthenticationError → bad API key (won't fix itself)
      - BadRequestError     → our request is wrong (won't fix itself)
    """
    last_error = None

    for attempt in range(max_retries):
        try:
            return client.messages.create(**kwargs)
        except anthropic.RateLimitError as e:
            last_error = e
            wait_time = 2 ** attempt  # 1s, 2s, 4s
            print(f"  ⏳ Rate limited. Waiting {wait_time}s... (attempt {attempt + 1}/{max_retries})")
            time.sleep(wait_time)
        except anthropic.APIConnectionError as e:
            last_error = e
            wait_time = 2 ** attempt
            print(f"  ⏳ Connection error. Retrying in {wait_time}s... (attempt {attempt + 1}/{max_retries})")
            time.sleep(wait_time)
        except anthropic.InternalServerError as e:
            last_error = e
            wait_time = 2 ** attempt
            print(f"  ⏳ Server error. Retrying in {wait_time}s... (attempt {attempt + 1}/{max_retries})")
            time.sleep(wait_time)
        except (anthropic.AuthenticationError, anthropic.BadRequestError):
            # These won't fix themselves — fail immediately
            raise

    # All retries exhausted
    raise last_error


def run_agent(user_message: str, messages: list):
    """Run the agent loop for a single user turn.

    This is the COMPLETE agent loop with all 5 lessons:
      1. Agent Loop     — while True: think → act → observe
      2. Tool Use       — notes, tasks, files, time
      3. Memory         — persistent facts + session history in system prompt
      4. Planning       — make_plan/update_plan for complex tasks
      5. Error Recovery — retry API calls, catch tool errors, guard against loops
    """

    client = anthropic.Anthropic()

    messages.append({"role": "user", "content": user_message})

    # ── BUILD SYSTEM PROMPT WITH MEMORY CONTEXT ──
    memory_context = build_memory_context()

    system_prompt = f"""You are a helpful personal assistant. You manage notes, tasks, files, and remember things about the user.

## Your Memory
{memory_context}

## Rules
- Use tools proactively. "Remember this" → save_memory. "I need to..." → add_task.
- For complex tasks (3+ steps), use make_plan FIRST, then execute each step.
- After each plan step, call update_plan to track progress.
- Save important facts about the user with save_memory (name, preferences, context).
- save_memory = facts about the user. save_note = content the user wants stored.
- Be concise. Confirm actions briefly, don't repeat content back.
- If a tool returns an error, try to recover or explain what went wrong."""

    # ── LOOP GUARD ──
    # LESSON 5 CONCEPT: Prevent infinite loops.
    # If Claude keeps calling tools without converging on an answer,
    # we force it to stop. This prevents runaway API costs.
    max_iterations = 15
    iteration = 0

    while iteration < max_iterations:
        iteration += 1

        # Use retry-enabled API call
        response = call_api_with_retry(
            client,
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            system=system_prompt,
            tools=ALL_TOOL_DEFINITIONS,
            messages=messages,
        )

        if response.stop_reason == "tool_use":
            messages.append({"role": "assistant", "content": response.content})

            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    # Log the tool call for transparency
                    input_preview = json.dumps(block.input, indent=None)[:80]
                    print(f"  🔧 {block.name}({input_preview})")

                    # Execute with error handling
                    result = execute_tool(block.name, block.input)
                    print(f"  📎 {result[:120]}")

                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result,
                    })

            messages.append({"role": "user", "content": tool_results})
            continue

        else:
            # Final text response
            assistant_text = ""
            for block in response.content:
                if hasattr(block, "text"):
                    assistant_text += block.text

            messages.append({"role": "assistant", "content": response.content})
            print(f"\n🤖 {assistant_text}")
            return messages

    # If we hit the loop limit, tell the user
    print("\n🤖 I got stuck in a loop and had to stop. Could you rephrase your request?")
    messages.append({
        "role": "assistant",
        "content": [{"type": "text", "text": "I reached my tool call limit. Please rephrase."}],
    })
    return messages


def main():
    print("=" * 50)
    print("  PERSONAL ASSISTANT AGENT")
    print("  Capabilities: notes, tasks, files, memory")
    print("  I remember you across sessions!")
    print("  Type 'quit' to exit")
    print("=" * 50)
    print()

    messages = []

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nSaving session...")
            save_session_summary(messages)
            print("Goodbye!")
            break

        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit", "q"):
            save_session_summary(messages)
            print("Session saved. Goodbye!")
            break

        print()
        messages = run_agent(user_input, messages)
        print()


if __name__ == "__main__":
    main()
