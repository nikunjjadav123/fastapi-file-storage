from pydantic  import BaseModel, constr, field_validator

class FileSchema(BaseModel):
    filename: constr(strip_whitespace=True, min_length=3, max_length=255)
    url: str
    size: int | None = None
    type: str | None = None

    @field_validator("filename")
    @classmethod
    def check_file_extension(cls, value):
        allowed_ext = (".png", ".jpg", ".jpeg")
        if not value.lower().endswith(allowed_ext):
            raise ValueError("Only image files are allowed")
        return value
    
    @field_validator("size")
    @classmethod
    def check_file_size(cls, value):
        max_size = 2 * 1024 * 1024  # 2 MB
        if value > max_size:
            raise ValueError("File size exceeds 2 MB limit")
        return value