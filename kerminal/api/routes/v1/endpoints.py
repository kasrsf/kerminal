from kerminal.core.services import MathService
from fastapi import APIRouter

router = APIRouter()


@router.get("/add")
async def add(a: float, b: float):
    """
    add parameters
    """
    result = MathService.add(a, b)
    return {"result": result}
