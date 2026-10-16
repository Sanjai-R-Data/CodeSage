from fastapi import FastAPI

app = FastAPI(
    title="CodeSage",
    description="AI-powered code review and security assistant.",
    version="0.1.0",
)


@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    """Return the application's health status."""
    return {
        "status": "healthy",
        "application": "CodeSage",
    }