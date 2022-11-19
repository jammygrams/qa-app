import os
import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from dotenv import load_dotenv

from utils import format_text_for_model

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

HUGGINGFACE_AUTH_TOKEN = os.environ.get("HUGGINGFACE_AUTH_TOKEN")

PRETRAINED_MODEL_NAME = "facebook/bart-large"
ADAPTER_MODEL_NAME = "jammygrams/bart-qa"
ADAPTER_NAME = "narrativeqa"

DEFAULT_TITLE = "Ghostbusters II"
DEFAULT_CONTEXT = """DANA (setting the wheel brakes on the buggy)
Thank you, Frank. I’ll get the hang of this eventually.
She continues digging in her purse while Frank leans
over the buggy and makes funny faces at the baby,
OSCAR, a very cute nine-month old boy.
FRANK (to the baby)
Hiya, Oscar. What do you say, slugger?
FRANK (to Dana)
That’s a good-looking kid you got there, Ms. Barrett."""
DEFAULT_QUESTION = "How is Oscar related to Dana?"


@st.cache(allow_output_mutation=True)
# TODO: type hint
def get_model():
    tokenizer = AutoTokenizer.from_pretrained(PRETRAINED_MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(
        ADAPTER_MODEL_NAME, use_auth_token=HUGGINGFACE_AUTH_TOKEN
    )
    model.set_active_adapters(ADAPTER_NAME)
    return tokenizer, model


tokenizer, model = get_model()

title = st.text_input("Title", DEFAULT_TITLE)
context = st.text_area("Body", DEFAULT_CONTEXT)
question = st.text_input("Question", DEFAULT_QUESTION)
button = st.button("Recalculate")

if question or button:
    user_input = format_text_for_model(title, context, question)
    # test_sample = tokenizer([user_input], truncation=True, max_length=1024, return_tensors='pt')
    tokenized_input = tokenizer([user_input], return_tensors="pt")
    prediction = prediction = model.generate(
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
    st.write("Answer: ", output)
