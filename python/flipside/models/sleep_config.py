from typing import Optional
from pydantic import BaseModel, Field


class SleepConfig(BaseModel):
    attempts: int = Field(..., description="Number of attempts")
    timeout_minutes: float = Field(..., description="Timeout in minutes")
    interval_seconds: Optional[float] = Field(None, description="Interval between attempts in seconds")

    model_config = {
        "validate_assignment": True,
    }
