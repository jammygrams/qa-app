from typing import Optional
from pydantic import BaseModel

class QuestionAnswerData(BaseModel):
    question: str
    title: Optional[str]
    document: str