from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

OUTPUT_PATH = "/usr/src/app/files/output.txt"

app = FastAPI(title="log-reader")

@app.on_event("startup")
async def start_reader() -> None:
    app.state.log_content = ""

@app.get("/", response_class=PlainTextResponse)
async def return_log() -> str:
    try:
        with open(OUTPUT_PATH, "r", encoding="utf-8") as output_file:
            app.state.log_content = output_file.read()
    except FileNotFoundError:
        app.state.log_content = "Log file not found."
    return app.state.log_content

@app.get("/status")
async def status() -> str:
    return "OK"
