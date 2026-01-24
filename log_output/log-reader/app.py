import asyncio
import random
from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI(title="log-reader")

async def log_loop():
    while True:
        app.state.log_line = get_log_line()
        print(app.state.log_line, flush=True)
        with open(OUTPUT_PATH, "r", encoding="utf-8") as output_file:
            pass
        await asyncio.sleep(5)


@app.on_event("startup")
async def start_logger() -> None:
    app.state.log_line = get_log_line()
    print(app.state.log_line, flush=True)
    asyncio.create_task(log_loop())

@app.get("/status")
async def status() -> str:
    return app.state.log_line
