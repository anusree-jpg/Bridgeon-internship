from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.get("/")
def auth_home():
    return {"message": "Auth working"}