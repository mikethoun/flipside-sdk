from typing import Optional
from pydantic import BaseModel, Field


class Tags(BaseModel):
    sdk_language: str
    sdk_package: str
    sdk_version: str
    user_tag: Optional[str] = Field(None)

    model_config = {
        "validate_assignment": True,
    }
