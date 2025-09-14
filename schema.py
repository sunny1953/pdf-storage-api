

from datetime import datetime
from typing import Dict, Any

def get_pdf_document(filename: str, content: bytes, size: int) -> Dict[str, Any]:
    return {
        "filename": filename,
        "content": content,
        "size": size,
        "upload_date": datetime.now()
    }

# ===========================================
# DATABASE AND COLLECTION NAMES
# ===========================================
# Change these names if you want different database/collection names

# Database name
DATABASE_NAME = "pdfs"

# Collection names
PDFS_COLLECTION = "pdfs_collection"
