from typing import Optional
from pydantic import BaseModel

class QuestionAnswerData(BaseModel):
    question: str
    title: str
    document: str