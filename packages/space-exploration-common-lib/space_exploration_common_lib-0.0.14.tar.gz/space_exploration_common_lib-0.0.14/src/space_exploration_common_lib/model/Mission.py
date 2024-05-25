from pydantic import BaseModel
from decimal import Decimal
from bson import Decimal128
from src.space_exploration_common_lib.model.Duration import Duration


class Mission(BaseModel):
    mission: str
    spacecraft_number: int
    call_sign: str
    astronaut: str
    launch_time: str
    launch_site: str
    duration: Duration
    orbits: int
    apogee_mi: int
    perigee_mi: int
    velocity_max_mph: int
    miss_mi: Decimal
    image_url: str

    def __init__(self, **data):
        if 'miss_mi' in data and isinstance(data['miss_mi'], Decimal128):
            data['miss_mi'] = Decimal(str(data['miss_mi']))
        super().__init__(**data)
