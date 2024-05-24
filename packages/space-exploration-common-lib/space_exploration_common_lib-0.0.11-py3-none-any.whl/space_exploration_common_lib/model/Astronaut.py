from pydantic import BaseModel
from typing import List

from ..model.enum.Programs import Programs
from ..model.enum.Missions import Missions


class Astronaut(BaseModel):
    name: str
    programs: List[Programs]
    missions: List[Missions]
    image_url: str
