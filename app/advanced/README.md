# Advanced Chat Flow

This folder is the start of a more advanced conversation pipeline for the project.

Implementation history is tracked in [phases/README.md](phases/README.md). The documented milestones currently are [01_simple_stateful_conversation_engine.md](phases/01_simple_stateful_conversation_engine.md), [02_layered_memory_context_architecture.md](phases/02_layered_memory_context_architecture.md), and [03_structured_memory_response_flow.md](phases/03_structured_memory_response_flow.md).

The advanced flow started as a simple stateful conversation memory and has now moved into a layered memory-driven architecture with structured memory:

- user facts can now be extracted into structured memory fields
- user and AI turns are stored in centralized memory state
- context is built as a structured object before prompt generation
- prompts are assembled through a dedicated prompt builder
- older turns can be compressed into summary memory
- recent turns stay available as short-term conversational context

## Run Reference

For environment setup, install commands, and a quick API test, use [phases/README.md](phases/README.md).

## Current Behavior

The active flow is now layered:

1. `main.py` exposes a `POST /chat-summary` endpoint.
2. `conversation_engine.py` appends the incoming prompt to `recent_messages`.
3. `context/context_builder.py` creates a structured context object from memory state.
4. `context/context_prompt.py` converts that context into model-ready messages.
5. The Ollama chat model generates the response from the structured prompt.
6. The response is appended back into memory and summarization may compress older turns.

This gives the assistant both short-term continuity and the first layer of long-term memory management without introducing a database yet.

## Folder Structure

- `main.py` contains the FastAPI entrypoint for the advanced chat route.
- `conversation_engine.py` orchestrates memory updates, context building, prompt building, model invocation, and summary checks.
- `context/memory_state.py` defines the shared in-memory conversation state.
- `context/context_builder.py` builds a structured context object from conversation state.
- `context/context_prompt.py` builds model-ready messages from structured context.
- `context/summary_memory.py` manages summarize triggers and long-term memory compression.
- `context/token_manager.py` is reserved for future token-budget management.
- `models/`, `prompts/`, and `retrieval/` are scaffolding for later expansion.

## Current State Model

The shared state currently looks like this:

```python
memory_state = {
    "user_profile": {},
    "goals": [],
    "projects": [],
    "summary": "",
    "recent_messages": [],
    "retrived_context": [],
}
```

Meaning:

- `user_profile` stores stable user attributes such as name.
- `goals` stores user goals extracted from conversation.
- `projects` stores user project information extracted from conversation.
- `summary` stores condensed long-term conversation memory.
- `recent_messages` stores the live short-term chat history.
- `retrived_context` is reserved for retrieved context that may later be merged into prompts.

## Limitations

- Memory is not persisted across restarts.
- There is no session separation, so all requests share the same in-process memory.
- Structured memory is not yet fully injected into context and prompt building.
- Retrieval-aware context is not wired into the advanced flow yet.
- Token management is not implemented yet.
- Summary retention is still controlled by a simple fixed-window policy.

## Next Likely Steps

- Add per-session memory instead of one global shared state.
- Inject structured memory fields into context and prompt assembly.
- Integrate retrieved context into the advanced pipeline.
- Add token-budget control before sending context to the model.
- Improve summary quality and memory retention rules.
- Add more structured memory categories beyond name, goal, and project.
