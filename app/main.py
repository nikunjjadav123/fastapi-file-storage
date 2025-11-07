# main.py
from fastapi import FastAPI,UploadFile, File
from fastapi.responses import FileResponse
from app.schemas import FileSchema
from app.file_manager import save_file, list_files
from app.config import UPLOAD_DIR
import os

app = FastAPI(title = "File Upload API")

@app.post("/upload", response_model=FileSchema)
async def upload_file(file: UploadFile = File(...)):
    file_path = save_file(file)
    url = f"/files/{file_path}"
    return {
        "filename": file.filename,
        "file_path": file_path,
        "url": url
    }

@app.get("/files", response_model=list[str])
async def get_files():
    return list_files()

@app.get("/files/{file_name}")
async def download_file(file_name: str):
    file_path = os.path.join(UPLOAD_DIR, file_name)
    if not os.path.exists(file_path):
        return {"error": "File not found"}
    
    return FileResponse(
        path=file_path,
        filename=file_name,
        media_type="application/octet-stream",
        headers={"Content-Disposition": f"attachment; filename={file_name}"}
    )
    # return FastAPIFileResponse(file_path)