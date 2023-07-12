from typing import Optional
from pydantic import BaseModel, Field
from datetime import date
from enum import Enum


class Priority(str, Enum):
    high = "high"
    medium = "medium"
    low = "low"


class Task(BaseModel):
    name: str = Field(min_length=1)
    description: str = Field(
        min_length=1,
        max_length=255,
    )
    priority: str = Priority
    start_date: date
    end_date: date
    status: bool = Field(default=False)


class TaskDetails(BaseModel):
    name: str = Field(min_length=1)
    description: str = Optional[str]
    priority: str = Optional[str]
