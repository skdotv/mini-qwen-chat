# Advanced Chat Flow

This folder is the start of a more advanced conversation pipeline for the project.

Implementation history is tracked in [phases/README.md](phases/README.md). The first documented milestone is [01_simple_stateful_conversation_engine.md](phases/01_simple_stateful_conversation_engine.md).

The first thing implemented here is a simple stateful conversation memory:

- User messages are stored in memory.
- AI responses are stored in memory.
- Each new request sends the accumulated recent conversation back to the model.
- The state currently lives in a process-local Python dictionary, so it resets when the app restarts.

## Run Reference

For environment setup, install commands, and a quick API test, use [phases/README.md](phases/README.md).

## Current Behavior

The active flow is small and intentionally simple:

1. `main.py` exposes a `POST /chat-summary` endpoint.
2. `conversation_engine.py` appends the incoming prompt to `recent_messages`.
3. The full recent message list is sent to the Ollama chat model.
4. The model response is appended back into memory and returned.

This gives the assistant short-term conversational continuity without needing a database or external memory store.

## Folder Structure

- `main.py` contains the FastAPI entrypoint for the advanced chat route.
- `conversation_engine.py` handles the stateful chat loop.
- `context/memory_state.py` defines the shared in-memory conversation state.
- `context/summary_memory.py` contains the summarize trigger logic.
- `context/context_builder.py` is reserved for future prompt/context assembly work.
- `context/token_manager.py` is reserved for future token-budget management.
- `models/`, `prompts/`, and `retrieval/` are scaffolding for later expansion.

## Current State Model

The shared state currently looks like this:

```python
memory_state = {
    "summary": "",
    "recent_messages": [],
    "retrived_messages": [],
}
```

Meaning:

- `summary` is reserved for condensed conversation memory.
- `recent_messages` stores the live turn-by-turn chat history.
- `retrived_messages` is reserved for retrieved context that may later be merged into prompts.

## Limitations

- Memory is not persisted across restarts.
- There is no session separation, so all requests share the same in-process memory.
- Summarization is not wired into the chat loop yet.
- Token management is not implemented yet.
- Retrieval-aware context assembly is not implemented yet.

## Next Likely Steps

- Trigger summarization after a configurable number of messages.
- Replace unbounded `recent_messages` growth with summary plus recent turns.
- Add per-session memory instead of one global shared state.
- Integrate retrieved context into the advanced pipeline.
- Add token-budget control before sending context to the model.
