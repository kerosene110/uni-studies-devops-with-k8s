import asyncio
import random
from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI(title="log-output")

ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyz"
RANDOM_STR = "".join(random.choice(ALPHABET) for _ in range(10))
OUTPUT_PATH = "/usr/src/app/files/output.txt"

def get_timestamp():
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace(
        "+00:00", "Z"
    )

def get_log_line(random_str=RANDOM_STR):
    return f"{get_timestamp()}: {random_str}"


async def log_loop():
    while True:
        app.state.log_line = get_log_line()
        with open(OUTPUT_PATH, "a", encoding="utf-8") as output_file:
            output_file.write(f"{app.state.log_line}\n")
        await asyncio.sleep(5)


@app.on_event("startup")
async def start_logger() -> None:
    app.state.log_line = get_log_line()
    print(app.state.log_line, flush=True)
    asyncio.create_task(log_loop())

@app.get("/status")
async def status() -> str:
    return app.state.log_line
