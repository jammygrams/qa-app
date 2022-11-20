import os
from dotenv import load_dotenv
from fastapi import FastAPI
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

from api.utils import format_text_for_model
from api.models import QuestionAnswerData

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

HUGGINGFACE_AUTH_TOKEN = os.environ.get("HUGGINGFACE_AUTH_TOKEN")

PRETRAINED_MODEL_NAME = "facebook/bart-large"
ADAPTER_MODEL_NAME = "jammygrams/bart-qa"
ADAPTER_NAME = "narrativeqa"

app = FastAPI(title="adapter-transformer for question answering, trained on ")

model, tokenizer = None, None

@app.on_event("startup")
def load_model():
  global model
  global tokenizer
  model = AutoModelForSeq2SeqLM.from_pretrained(
        ADAPTER_MODEL_NAME, use_auth_token=HUGGINGFACE_AUTH_TOKEN
    )
  tokenizer = AutoTokenizer.from_pretrained(PRETRAINED_MODEL_NAME)
  model.set_active_adapters(ADAPTER_NAME)

@app.post("/api", tags=["prediction"])
async def get_prediction(data: QuestionAnswerData):
  question, title, document = dict(data)["question"], dict(data)["title"], dict(data)["document"]
  input_string = format_text_for_model(title, document, question)
  # test_sample = tokenizer([user_input], truncation=True, max_length=1024, return_tensors='pt')
  tokenized_input = tokenizer([input_string], return_tensors="pt")
  prediction = model.generate(
      tokenized_input.input_ids,
      num_beams=5,
      return_dict_in_generate=True,
      output_scores=True,
      max_length=50,
  )
  output = tokenizer.decode(
      prediction["sequences"][0], # single prediction
      skip_special_tokens=True,
      clean_up_tokenization_spaces=True,
  )
  return output