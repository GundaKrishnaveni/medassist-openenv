from pydantic import BaseModel
from typing import List

class Observation(BaseModel):
    symptoms: List[str]
    patient_info: str

class Action(BaseModel):
    decision: str

class Reward(BaseModel):
    score: float
