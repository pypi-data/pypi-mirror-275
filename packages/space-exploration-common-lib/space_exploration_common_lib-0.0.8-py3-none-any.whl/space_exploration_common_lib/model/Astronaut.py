from pydantic import BaseModel


class Astronaut(BaseModel):
    name: str
