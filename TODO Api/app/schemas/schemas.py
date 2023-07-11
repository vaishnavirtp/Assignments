from typing import Optional
from pydantic import BaseModel, Field
from datetime import date


class Task(BaseModel):
    name: str = Field(min_length=1)
    description: str = Field(
        min_length=1,
        max_length=255,
    )
    priority: str = Field(min_length=1, max_length=20)
    start_date: date
    end_date: date
    status: bool = Field(default=False)


class TaskDetails(BaseModel):
    name: str = Field(min_length=1)
    description: str = Optional[str]
