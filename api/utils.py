import requests

from api.models import QuestionAnswerData

def format_text_for_model(title: str, context: str, question: str) -> str:
    question = "<question> " + question.strip()
    title = " <title> " + title.strip()
    context = " <document> " + context.strip().replace("\n", " ")
    return question + " " + title + " " + context

def query_api(url: str, title: str, context: str, question: str):
    input_data = QuestionAnswerData(question = question, title=title, document=context)
    response = requests.post(url = url, data= dict(input_data))
    return response.json()