import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_DIR = os.path.join(BASE_DIR, "files")

os.makedirs(UPLOAD_DIR, exist_ok=True)