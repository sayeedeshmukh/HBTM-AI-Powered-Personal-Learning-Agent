from pydantic import BaseModel


class ResourceInput(BaseModel):
    topic: str
    skill_level: str
    learning_style: str