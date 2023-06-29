from fastapi import APIRouter
from typing import Optional

router = APIRouter()
0, 1, 1, 2, 3, 5, 8, 13
def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

@router.get("/fibonacci/{n}")
async def get_fibonacci(n: int):
    return {"nth Fibonacci number": fibonacci(n)}
