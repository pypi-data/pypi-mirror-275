from pydantic import BaseModel
from typing import List


class Program(BaseModel):
    program_name: str
    mission_names: List[str]
    image_url: str
