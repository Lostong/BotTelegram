from pydantic import BaseModel

class Missions_model(BaseModel):
    name: str
    description: str
    how_to_achieve: str
