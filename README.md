# question answering (qa) app
Goal: test out question answering performance
#### To run:
1. serve hugging face model with fast api on google colab (what a hack)
    * Run `qaapi/serve_adaptor_transformer.ipynb` on google colab, which will give a **ngrok url**
2. run streamlit app
    * Run streamlit app...
        * locally, `python -m streamlit run streamlit_app/app.py` (opening with `streamlit ...` doesn't work strangely)
        * Or on access on streamlit cloud: 
    * past the **ngrok url** into the streamlit app 