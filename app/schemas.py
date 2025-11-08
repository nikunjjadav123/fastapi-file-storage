from pydantic  import BaseModel, constr, field_validator

class FileSchema(BaseModel):
    filename: str
    url: str | None = None
    size: int | None = None
    type: str | None = None

    @field_validator("filename")
    @classmethod
    def check_file_extension(cls, value):
        allowed_ext = (".png", ".jpg", ".jpeg")
        if not value.lower().endswith(allowed_ext):
            raise ValueError("Only image files are allowed")
        return value
    
    