from pydantic import BaseModel


class SupervisorInput(BaseModel):
    topic: str
    percentage: float
    performance: str
    current_index: int
    roadmap: list
    learning_style: str
    skill_level: str