from pydantic import BaseModel, Field
from typing import Optional, Dict, List


class ExtractedFields(BaseModel):
    Name: str = Field(..., max_length=200)
    Summary: str
    Contact: Dict[str, str]
    Online_Profiles: Optional[list]
    Skills: list
    Years_of_Experience: int
    Experience: Optional[list]
    Roles: list
    Education: list
    Certifications: Optional[list]
    Projects: Optional[list]
    Other: Optional[list]
