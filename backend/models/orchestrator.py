from pydantic import BaseModel


class OrchestratorInput(BaseModel):
    goal: str
    skill_level: str
    daily_hours: float
    deadline: str
    learning_style: str