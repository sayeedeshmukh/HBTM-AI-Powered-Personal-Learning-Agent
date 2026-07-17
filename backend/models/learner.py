from pydantic import BaseModel


class LearnerInput(BaseModel):
    goal: str
    skill_level: str
    daily_hours: float
    deadline: str
    learning_style: str
    notes: str = ""