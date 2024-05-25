from pydantic import BaseModel
from typing import List


class MissionNames(BaseModel):
    mission_names: List[str]
