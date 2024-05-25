from pydantic import BaseModel


class Program(BaseModel):
    program: str
    image_url: str
