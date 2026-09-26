from fastapi import FastAPI
from backend.app.api.router import api_router 

app = FastAPI(title="FlowPilot AI")

app.include_router(api_router, prefix="/api/v1")

