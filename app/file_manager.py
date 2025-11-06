import os
from fastapi import UploadFile
from app.config import UPLOAD_DIR

def save_file(file: UploadFile) -> str:
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb+") as file_object:
        file_object.write(file.file.read())
    return file.filename

def list_files() -> list:
    return os.listdir(UPLOAD_DIR)
