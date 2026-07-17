from pydantic import BaseModel
from typing import List


class Answer(BaseModel):
    question_id: int
    selected_option: str


class EvaluationInput(BaseModel):
    topic: str
    answers: List[Answer]