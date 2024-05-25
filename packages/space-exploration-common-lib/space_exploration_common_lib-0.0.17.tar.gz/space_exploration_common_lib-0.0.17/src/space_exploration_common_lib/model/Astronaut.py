from pydantic import BaseModel
from typing import List


class Astronaut(BaseModel):
    first_name: str
    last_name: str
    programs: List[str]
    missions: List[str]
    image_url: str
