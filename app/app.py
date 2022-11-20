import streamlit as st

from api.utils import query_api

API_URL = "https://d061-34-91-64-246.ngrok.io/api"

DEFAULT_TITLE = "Ghostbusters II"
DEFAULT_CONTEXT = "DANA (setting the wheel brakes on the buggy) Thank you, Frank. I’ll get the hang of this eventually. She continues digging in her purse while Frank leans over the buggy and makes funny faces at the baby, OSCAR, a very cute nine-month old boy. FRANK (to the baby) Hiya, Oscar. What do you say, slugger? FRANK (to Dana) That’s a good-looking kid you got there, Ms. Barrett."
DEFAULT_QUESTION = "How is Oscar related to Dana?"

title = st.text_input("Title", DEFAULT_TITLE)
context = st.text_area("Body", DEFAULT_CONTEXT)
question = st.text_input("Question", DEFAULT_QUESTION)
button = st.button("Recalculate")

if question or button:
    response = query_api(url=API_URL, question=question, context=context, title=title)

    st.write("Answer:\n", response)
