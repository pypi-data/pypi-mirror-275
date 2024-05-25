from pydantic import BaseModel

from ..mission.MissionNames import MissionNames


class Program(BaseModel):
    program_name: str
    mission_names: MissionNames
    image_url: str
