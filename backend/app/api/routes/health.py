from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def get_health():
    return {
        "status": 200,
        "message": "Fetched Successfully!"
     }