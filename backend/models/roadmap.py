from pydantic import BaseModel
from typing import List


class PlannerInput(BaseModel):
    goal: str
    goal_category: str
    domain: str
    target_role: str
    current_skill_level: str
    difficulty: str
    deadline_feasible: bool
    recommended_timeline: str
    required_skills: List[str]
    missing_prerequisites: List[str]
    learning_constraints: List[str]
    priority_topics: List[str]
    summary: str