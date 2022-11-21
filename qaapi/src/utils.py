import requests

from qaapi.src.models import QuestionAnswerData


def format_text_for_model(title: str, document: str, question: str) -> str:
    question = "<question> " + question.strip()
    title = " <title> " + title.strip()
    document = " <document> " + document.strip().replace("\n", " ")
    return question + " " + title + " " + document


def query_api(url: str, title: str, document: str, question: str):
    headers = {"accept": "application/json"}
    data = QuestionAnswerData(question=question, title=title, document=document)
    json_data = dict(data)
    response = requests.post(url=url, headers=headers, json=json_data)
    return response.json()
