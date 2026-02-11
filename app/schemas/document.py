from pydantic import BaseModel
from datetime import datetime

class DocumentResponse(BaseModel):
    id: int
    filename: str
    file_type: str
    created_at: datetime

    class Config:
        orm_mode = True


class DocumentDetailResponse(DocumentResponse):
    raw_text: str

class DocumentUpdateRequest(BaseModel):
    raw_text: str