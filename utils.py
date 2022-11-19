def format_text_for_model(title: str, context: str, question: str) -> str:
    question = "<question> " + question.strip()
    title = " <title> " + title.strip()
    context = " <document> " + context.strip().replace("\n", " ")
    return question + " " + title + " " + context