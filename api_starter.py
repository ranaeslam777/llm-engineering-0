import asyncio
import time
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="LLM Foundation API")


class PromptRequest(BaseModel):
    prompt: str = Field(..., min_length=3, description="User prompt text")
    models: list[str] = Field(default=["gpt-mini", "claude-haiku"])


class ModelResponse(BaseModel):
    model: str
    latency_sec: float
    output: str


class MultiModelResult(BaseModel):
    total_time_sec: float
    responses: list[ModelResponse]


async def query_model(model_name: str, prompt: str) -> ModelResponse:
    start = time.time()
    delay = 1.2 if "mini" in model_name or "haiku" in model_name else 2.5
    await asyncio.sleep(delay)
    elapsed = round(time.time() - start, 2)
    return ModelResponse(
        model=model_name,
        latency_sec=elapsed,
        output=f"[{model_name}] processed : {prompt[:40]}",
    )


@app.post("/generate", response_model=MultiModelResult)
async def generate_responses(request: PromptRequest):
    t0 = time.time()
    tasks = [query_model(m, request.prompt) for m in request.models]
    results = await asyncio.gather(*tasks)
    total = round(time.time() - t0, 2)
    return MultiModelResult(total_time_sec=total, responses=results)
