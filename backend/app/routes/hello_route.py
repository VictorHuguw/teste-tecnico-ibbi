from fastapi import APIRouter
from app.controllers.hello_controller import get_hello_message

router = APIRouter()

@router.get("/hello")
def read_hello():
    return get_hello_message()
