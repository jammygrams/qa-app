import streamlit as st

# TODO: need relative path for now to run on streamlit cloud 
from ..qaapi.src.utils import query_api

DEFAULT_TITLE = "Ghostbusters II"
DEFAULT_DOCUMENT = "DANA (setting the wheel brakes on the buggy) Thank you, Frank. I’ll get the hang of this eventually. She continues digging in her purse while Frank leans over the buggy and makes funny faces at the baby, OSCAR, a very cute nine-month old boy. FRANK (to the baby) Hiya, Oscar. What do you say, slugger? FRANK (to Dana) That’s a good-looking kid you got there, Ms. Barrett."
DEFAULT_QUESTION = "How is Oscar related to Dana?"

url = st.text_input("API URL", placeholder="e.g. https://5385-34-91-64-246.ngrok.io")
title = st.text_input("Title", DEFAULT_TITLE)
document = st.text_area("Body", DEFAULT_DOCUMENT)
question = st.text_input("Question", DEFAULT_QUESTION)
button = st.button("Recalculate")

if url and (question or button):
    api_url = f"{url}/api"
    response = query_api(url=api_url, question=question, document=document, title=title)

    st.write("Answer:\n", response)
