from pydantic import BaseModel
from typing import List
from .Mission import Mission


class Program(BaseModel):
    name: str
    missions: List[Mission]
    image_url: str
