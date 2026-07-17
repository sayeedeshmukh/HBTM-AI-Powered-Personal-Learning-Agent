from pydantic import BaseModel


class QuizInput(BaseModel):
    topic: str
    difficulty: str
    num_questions: int = 5