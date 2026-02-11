import asyncio
from typing import override
from kosong.tooling import CallableTool2, ToolOk, ToolReturnValue
from pydantic import BaseModel

class CompareParams(BaseModel):
    """
    CompareParams class.
    """
    a: float
    b: float

class PanicParams(BaseModel):
    """
    PanicParams class.
    """
    message: str

class Panic(CallableTool2[PanicParams]):
    """
    Panic class.
    """
    name: str = "panic"
    description: str = "Raise an exception to cause the tool call to fail."
    params: type[PanicParams] = PanicParams

    @override
    async def __call__(self, params: PanicParams) -> ToolReturnValue:
        await asyncio.sleep(2)
        raise Exception(f"panicked with a message with {len(params.message)} characters")

class Compare(CallableTool2[CompareParams]):
    """
    Compare class.
    """
    name: str = "compare"
    description: str = "Compare two numbers"
    params: type[CompareParams] = CompareParams

    @override
    async def __call__(self, params: CompareParams) -> ToolReturnValue:
        if params.a > params.b:
            return ToolOk(output="greater")
        elif params.a < params.b:
            return ToolOk(output="less")
        else:
            return ToolOk(output="equal")

class PlusParams(BaseModel):
    """
    PlusParams class.
    """
    a: float
    b: float

class Plus(CallableTool2[PlusParams]):
    """
    Plus class.
    """
    name: str = "plus"
    description: str = "Add two numbers"
    params: type[PlusParams] = PlusParams

    @override
    async def __call__(self, params: PlusParams) -> ToolReturnValue:
        return ToolOk(output=str(params.a + params.b))
