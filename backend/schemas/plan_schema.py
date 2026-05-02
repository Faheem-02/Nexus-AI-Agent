from typing import Any

from pydantic import BaseModel


class Step(BaseModel):
    id: str
    task: str
    tool: str
    input: Any


class Plan(BaseModel):
    steps: list[Step]
