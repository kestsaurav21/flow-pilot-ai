# from fastapi import FastAPI
# from backend.app.api.router import api_router 

# app = FastAPI(title="FlowPilot AI")

# app.include_router(api_router, prefix="/api/v1")

from fastapi import FastAPI
from sqlalchemy import text

from app.api.router import api_router
from app.core.database import engine

app = FastAPI(title="FlowPilot AI")

app.include_router(
    api_router,
    prefix="/api/v1",
)


@app.get("/api/v1/db-health")
def database_health():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"database": result.scalar()}