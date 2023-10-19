from typing import Dict
from pydantic import BaseModel


class TTSIn(BaseModel):
    text: str
    role: str='default'
    # price: float
    # tax: float | None = None

class TTSOut(BaseModel):
    success:bool
    code:int
    message:Dict
