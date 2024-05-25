from pydantic import BaseModel
from typing import List
from .Program import Program
from .Mission import Mission


class Astronaut(BaseModel):
    first_name: str
    last_name: str
    programs: List[Program]
    missions: List[Mission]
    image_url: str
