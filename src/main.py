from fastapi import FastAPI
from src.blog.routers import router as blogRouter
from src.config import settings

app = FastAPI(
    title=settings.app_name
)

app.include_router(blogRouter)
