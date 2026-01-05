import os

from fastapi import FastAPI

app = FastAPI(title="todo-app")


@app.on_event("startup")
async def announce_startup() -> None:
    port_env = os.getenv("PORT")
    if not port_env:
        print("Warning: PORT is not set.")
        raise SystemExit(1)
    print(f"Server started in port {port_env}")


@app.get("/")
async def root() -> str:
    return "Todo app is running with Ingress"
