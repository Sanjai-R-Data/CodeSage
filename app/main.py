
from typing import Annotated

from fastapi import FastAPI, File, HTTPException, UploadFile

from app.validators import SourceValidationError, validate_source


app = FastAPI(
    title="CodeSage",
    description="AI-powered code review and security assistant.",
    version="0.1.0",
)

MAX_SOURCE_SIZE = 1_000_000


@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    """Return the application's health status."""
    return {
        "status": "healthy",
        "application": "CodeSage",
    }


@app.post("/validate-source", tags=["Source Validation"])
async def validate_python_source(
    file: Annotated[UploadFile, File(description="Python source file")],
) -> dict[str, object]:
    """Validate an uploaded Python source file without executing it."""

    try:
        filename = file.filename or ""

        # Read at most one byte beyond the limit to detect oversized uploads.
        content = await file.read(MAX_SOURCE_SIZE + 1)

        if len(content) > MAX_SOURCE_SIZE:
            raise HTTPException(
                status_code=413,
                detail="Source file exceeds the 1 MB limit.",
            )

        try:
            result = validate_source(filename, content)
        except SourceValidationError as exc:
            raise HTTPException(
                status_code=400,
                detail=str(exc),
            ) from exc

        return {
            "valid": True,
            "filename": result.filename,
            "size_bytes": result.size_bytes,
            "message": "Python source passed input validation.",
        }
    finally:
        await file.close()
