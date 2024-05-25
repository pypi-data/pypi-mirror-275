from pydantic import BaseModel
from typing import List


class Astronaut(BaseModel):
    astronaut_first_name: str
    astronaut_last_name: str
    program_names: List[str]
    mission_names: List[str]
    image_url: str
