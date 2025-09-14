from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router
from database import test_connection
import os

app = FastAPI(
    title="PDF Storage API - API Only",
    description="A secure API for storing, viewing, and downloading PDF files. API key required for all operations.",
    version="1.0.0"
)

# Add CORS middleware for cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your friend's domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files and templates (removed for API-only access)
# app.mount("/static", StaticFiles(directory="static"), name="static")
# templates = Jinja2Templates(directory="templates")

# Include API routes
app.include_router(router)

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "PDF Storage API is running"}

# Home route - API only, no web interface
@app.get("/")
async def home():
    return {
        "message": "PDF Storage API - API Only Access",
        "documentation": "/docs",
        "api_key_endpoint": "/get-api-key",
        "note": "This is an API-only service. Use the API endpoints with your API key."
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
