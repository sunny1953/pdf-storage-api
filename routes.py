from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from database import pdfs_collection
from models import PDFInfo, PDFResponse
from schema import get_pdf_document
from typing import List
import io
from bson import ObjectId

router = APIRouter()

@router.post("/upload", response_model=PDFResponse)
async def upload_pdf(file: UploadFile = File(...)):
    # Check if file is PDF
    if not file.content_type == "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    # Check file size (10MB limit)
    content = await file.read()
    if len(content) > 10 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File too large. Maximum size is 10MB")
    
    # Store in MongoDB
    pdf_doc = get_pdf_document(file.filename, content, len(content))
    result = await pdfs_collection.insert_one(pdf_doc)
    
    return PDFResponse(
        message="PDF uploaded successfully to MongoDB",
        pdf_id=str(result.inserted_id)
    )

@router.get("/pdfs", response_model=List[PDFInfo])
async def get_pdfs():
    pdfs = []
    async for pdf in pdfs_collection.find({}, {"filename": 1, "upload_date": 1, "size": 1}):
        pdfs.append(PDFInfo(
            id=str(pdf["_id"]),
            filename=pdf["filename"],
            upload_date=pdf["upload_date"],
            size=pdf["size"]
        ))
    
    # Sort by upload date (newest first)
    pdfs.sort(key=lambda x: x.upload_date, reverse=True)
    return pdfs

@router.get("/view/{pdf_id}")
async def view_pdf(pdf_id: str):
    try:
        pdf = await pdfs_collection.find_one({"_id": ObjectId(pdf_id)})
        if not pdf:
            raise HTTPException(status_code=404, detail="PDF not found")
        
        return StreamingResponse(
            io.BytesIO(pdf["content"]),
            media_type="application/pdf",
            headers={"Content-Disposition": f"inline; filename={pdf['filename']}"}
        )
    except Exception as e:
        raise HTTPException(status_code=404, detail="Invalid PDF ID format")

@router.get("/download/{pdf_id}")
async def download_pdf(pdf_id: str):
    try:
        pdf = await pdfs_collection.find_one({"_id": ObjectId(pdf_id)})
        if not pdf:
            raise HTTPException(status_code=404, detail="PDF not found")
        
        return StreamingResponse(
            io.BytesIO(pdf["content"]),
            media_type="application/pdf",
            headers={"Content-Disposition": f"attachment; filename={pdf['filename']}"}
        )
    except Exception as e:
        raise HTTPException(status_code=404, detail="Invalid PDF ID format")

@router.delete("/pdf/{pdf_id}")
async def delete_pdf(pdf_id: str):
    try:
        result = await pdfs_collection.delete_one({"_id": ObjectId(pdf_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="PDF not found")
        
        return {"message": "PDF deleted successfully from MongoDB"}
    except Exception as e:
        raise HTTPException(status_code=404, detail="Invalid PDF ID format")
