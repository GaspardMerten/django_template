from ninja import Router
from pydantic import BaseModel

router = Router(
    tags=["hello"],
)


class HelloDataOut(BaseModel):
    hello: str = "world"


@router.get("/hello", response=HelloDataOut)
def hello_world(request):
    return {"hello": "world"}
