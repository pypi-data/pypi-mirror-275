from pydantic import BaseModel
from typing import List


class Astronaut(BaseModel):
    astronaut_first_name: str
    astronaut_last_name: str
    programs: List[str]
    image_url: str
