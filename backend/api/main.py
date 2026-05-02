import asyncio
import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from control_loop.loop import run_loop
from executor.executor import Executor
from planner.planner import Planner

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RunAgentRequest(BaseModel):
    goal: str


@app.post("/run-agent")
def run_agent(request: RunAgentRequest):
    planner = Planner()
    executor = Executor()

    plan = planner.create_plan(request.goal)
    results = run_loop(plan.model_dump(), executor)

    return {"plan": plan.model_dump(), "results": results}
