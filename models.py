from pydantic import BaseModel
from datetime import datetime
from typing import List

class PDFInfo(BaseModel):
    id: str
    filename: str
    upload_date: datetime
    size: int

class PDFResponse(BaseModel):
    message: str
    pdf_id: str

class PDFUpload(BaseModel):
    filename: str
    content: bytes
    size: int
    upload_date: datetime
