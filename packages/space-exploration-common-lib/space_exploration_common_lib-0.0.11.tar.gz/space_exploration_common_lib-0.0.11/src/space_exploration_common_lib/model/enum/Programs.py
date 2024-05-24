from enum import Enum
from pydantic import BaseModel


class Programs(str, Enum):
    MERCURY = "Mercury"
    GEMINI = "Gemini"
    APOLLO = "Apollo"


class ProgramsModel(BaseModel):
    program: Programs
