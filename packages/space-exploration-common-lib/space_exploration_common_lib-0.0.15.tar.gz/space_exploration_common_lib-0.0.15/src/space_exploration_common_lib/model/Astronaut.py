from pydantic import BaseModel
from typing import List

from ..model.enum.Programs import Programs


class Astronaut(BaseModel):
    first_name: str
    last_name: str
    programs: List[Programs]
    missions: List[str]
    image_url: str
