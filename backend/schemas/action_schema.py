from typing import Any

from pydantic import BaseModel


class Action(BaseModel):
    tool: str
    action: str
    input: Any
