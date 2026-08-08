import uvicorn
from app.core.config import settings

# uv run uvicorn app.main:app
if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=True
    )