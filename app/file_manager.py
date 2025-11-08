import os
from fastapi import HTTPException, UploadFile
import magic
from app.config import UPLOAD_DIR
from app.schemas import FileSchema

async def save_file(file: UploadFile) -> str:

    contents = await file.read()
    size = len(contents)
    # Step 1: Real MIME type validation
    mime = magic.from_buffer(contents, mime=True)
    allowed_mimes = ["image/png", "image/jpeg", "image/jpg"]
    
    if mime not in allowed_mimes:
         raise HTTPException(
            status_code=400,
            detail=f"Invalid content type: {mime}. Only image files are allowed."
        )
    
    # Step 2: Pydantic validation (extension + size)
    validated = FileSchema(filename=file.filename, size=size)
    try:
        # Step 3: Save file only if all validations passed
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb+") as file_object:
            file_object.write(contents)
        return file.filename
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

def list_files() -> list:
    return os.listdir(UPLOAD_DIR)
