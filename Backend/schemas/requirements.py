from pydantic import BaseModel, Field
from typing import Optional


class Requirements(BaseModel):
    Role: Optional[str]
    Skills: Optional[list[str]] = Field(...)
    Years_of_Experience: Optional[int]
