from typing import Optional
from pydantic import BaseModel, Field, validator
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

    @validator("start_date", "end_date", pre=True)
    def validate_date(cls, value):
        if not isinstance(value, date):
            print("error")
            raise ValueError("Invalid Input Data")
        return value

    @validator("name", "description", "priority", pre=True)
    def validate_strings(cls, value):
        if not isinstance(value, str):
            raise ValueError("Invalid Input Data")
        return value


class TaskDetails(BaseModel):
    name: str = Field(min_length=1)
    description: str = Optional[str]
    priority: str = Optional[Priority]
