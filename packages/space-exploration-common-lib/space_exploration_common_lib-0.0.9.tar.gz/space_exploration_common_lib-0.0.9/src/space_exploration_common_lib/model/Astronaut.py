from pydantic import BaseModel
from typing import List


class Astronaut(BaseModel):
    name: str
    programs: List[str]
