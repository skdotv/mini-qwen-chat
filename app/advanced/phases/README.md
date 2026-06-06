# Advanced Phases

This folder keeps a running history of the implementation phases completed inside `app/advanced`.

Use it as a build log:

- Each phase gets its own Markdown file.
- File names must start with a zero-padded numeric prefix so ordering stays stable.
- Keep the format chronological: `01_...`, `02_...`, `03_...`.
- Each file should describe what was built, how it works, current limits, and what the next phase should solve.

## Naming Convention

Use this format for every new phase file:

```text
01_phase_name.md
02_phase_name.md
03_phase_name.md
```

## Current Sequence

- `01_simple_stateful_conversation_engine.md`
- `02_layered_memory_context_architecture.md`

The goal is to preserve implementation history in order, not just the latest state.

## Environment Setup

```bash
cd /Users/vinodkhadka/Documents/AI/mini-qwen-chat
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn langchain-ollama langchain-core pydantic
ollama pull qwen2.5-coder:7b-instruct-q6_K
```

## Run The Advanced App

```bash
uvicorn app.advanced.main:app --reload
```

## Quick API Test

```bash
curl -X POST http://127.0.0.1:8000/chat-summary \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Hello"}'
```

Use the phase files for detailed implementation history and diagrams.
