from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from app.core.base import Base
from app.routers import buildings, activities, organizations
from app.database import engine
from app.core.config import settings

api_key_header = APIKeyHeader(name=settings.API_KEY_NAME, auto_error=False)


async def get_api_key(api_key: str = Depends(api_key_header)):
    if api_key != settings.API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API Key"
        )
    return api_key


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(dependencies=[Depends(get_api_key)], lifespan=lifespan)


app.include_router(buildings.router)
app.include_router(activities.router)
app.include_router(organizations.router)


@app.get("/")
def read_root():
    return {"message": "Organization API"}
