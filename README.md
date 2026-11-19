# LLM Engineering — Level 0 Foundations

Starter experiments and API foundations for LLM engineering workflows, focusing on concurrent model calls, schema validation, and latency tracking.

## What Is Inside

- `1.py`: Async concurrency test using `asyncio` and `asyncio.gather` to simulate multiple LLM calls in parallel and compare execution time.
- `api_starter.py`: FastAPI service with Pydantic request/response schemas (`PromptRequest`, `ModelResponse`, `MultiModelResult`), input length validation, simulated model latency, and total execution time measurement.

## Setup and Run

```bash
python -m venv venv
# Windows (PowerShell):
.\venv\Scripts\Activate.ps1

pip install fastapi uvicorn pydantic
uvicorn api_starter:app --reload 