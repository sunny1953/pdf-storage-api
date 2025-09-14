# PDF Storage App

A simple FastAPI application for storing, viewing, and downloading PDF files using MongoDB Atlas.

## Features

- Upload PDF files (up to 10MB)
- View PDFs in browser
- Download PDFs
- Delete PDFs
- Simple web interface

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Update MongoDB connection string in `main.py`:
   - Replace `YOUR_MONGODB_CONNECTION_STRING_HERE` with your actual MongoDB Atlas connection string

3. Run the application:
```bash
python main.py
```

4. Open your browser and go to: `http://localhost:8000`

## API Endpoints

- `GET /` - Web interface
- `POST /upload` - Upload PDF file
- `GET /pdfs` - Get list of all PDFs
- `GET /view/{pdf_id}` - View PDF in browser
- `GET /download/{pdf_id}` - Download PDF
- `DELETE /pdf/{pdf_id}` - Delete PDF

## MongoDB Connection

You need to provide your MongoDB Atlas connection string in the `main.py` file. The app will automatically create a database called `pdf_storage` and a collection called `pdfs`.
