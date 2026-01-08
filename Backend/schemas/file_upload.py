from pydantic import BaseModel, Field


class FileUpload(BaseModel):
    filename: str = Field(..., max_length=200)
    content_type: str
    file_size: int
