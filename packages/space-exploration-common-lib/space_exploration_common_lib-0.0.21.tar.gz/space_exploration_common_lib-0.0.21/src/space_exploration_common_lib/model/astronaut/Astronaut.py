from pydantic import BaseModel
from typing import List

from ..program.ProgramNames import ProgramNames


class Astronaut(BaseModel):
    astronaut_first_name: str
    astronaut_last_name: str
    program_names: List[ProgramNames]
    image_url: str
