import asyncio
import time


async def ask_llm(model_name: str, delay: int):
    print(f"Sending a request to {model_name}...")
    await asyncio.sleep(delay)
    print(f"Got the response from {model_name} after {delay} a second !")
    return f"result {model_name}"


async def main():
    start_time = time.time()

    results = await asyncio.gather(
        ask_llm("GPT-Model", 3),
        ask_llm("Claude-Model", 2),
        ask_llm("Llama-Model", 4)
    )

    end_time = time.time()
    print(f"The final results : {results}")
    print(f"The needed time :{round(end_time - start_time, 2)} seconds only!")

if __name__ == "__main__":
    asyncio.run(main())
