from pydantic import BaseModel

class NudgeInput(BaseModel):
    goal: str
    topic: str
    inactivity_days: int
