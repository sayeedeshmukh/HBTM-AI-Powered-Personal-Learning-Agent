from pydantic import BaseModel
from typing import List


class WrongAnswer(BaseModel):
    question: str
    correct_answer: str
    your_answer: str


class CoachInput(BaseModel):
    topic: str
    score: int
    total_questions: int
    percentage: float
    performance: str
    incorrect_answers: List[WrongAnswer]