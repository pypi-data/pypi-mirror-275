from pydantic import BaseModel
from typing import List


class AstronautNames(BaseModel):
    astronaut_names: List[str]

