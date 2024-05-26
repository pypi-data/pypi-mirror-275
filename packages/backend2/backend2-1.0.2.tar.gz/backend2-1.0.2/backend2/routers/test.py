from fastapi import APIRouter, Depends
from backend2.auth.auth_bearer import JWTBearer

router = APIRouter(
    prefix="/backend2",
)

@router.get("/hello_backend2")
async def hello_world():
    return {"message": "Welcome to backend2!"}


@router.get("/test_backend2_authenticaton", dependencies=[Depends(JWTBearer())])
async def test_authentication():
    return {"message": "Authentication successfull"}
