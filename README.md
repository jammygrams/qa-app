# question answering (qa) app
**Goal: test out question answering performance**
#### To run:
1. serve hugging face model with fast api on google colab (what a hack)
    * Run `qaapi/serve_adaptor_transformer.ipynb` on google colab, which will give a **ngrok url**
    * Reference: https://www.youtube.com/watch?v=7-igAakUUTY
2. run streamlit app
    * Run streamlit app...
        * locally, `python -m streamlit run streamlit_app/app.py` (opening with `streamlit ...` doesn't work strangely)
        * TODO: streamlit cloud.  Doesn't work with multiple folders?
    * past the **ngrok url** into the streamlit app 