from pydantic import BaseModel
from typing import List
from ..mission.MissionNames import MissionNames


class ProgramNames(BaseModel):
    program_names: List[str, MissionNames]
