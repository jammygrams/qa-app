# question answering (qa) app
**Goal: test out question answering performance**
#### To run:
1. serve hugging face model with fast api on google colab (what a hack)
    * Run `qaapi/serve_adaptor_transformer.ipynb` on google colab, which will give a **ngrok url**
    * Reference: https://www.youtube.com/watch?v=7-igAakUUTY
2. run streamlit app
    * Run streamlit app...
        * locally, `python -m streamlit run streamlit_app/app.py` (opening with `streamlit ...` doesn't work strangely)
        * Run on GCP at `https://streamlit-sm2m6pkoaq-od.a.run.app`
            * see `https://console.cloud.google.com/run/detail/europe-west9/streamlit/revisions?project=qa-app-369311`
    * paste the **ngrok url** into the streamlit app 


#### Building docker image for Streamlit app on GCP
Ref: https://www.artefact.com/blog/how-to-deploy-and-secure-your-streamlit-app-on-gcp/
1. `docker build -t eu.gcr.io/qa-app-369311/streamlit:v1 -f streamlit_app/dockerfile .`
1. `docker run -p 8080:8080 eu.gcr.io/qa-app-369311/streamlit:v2` to make sure it works
1. `docker push eu.gcr.io/qa-app-369311/streamlit:v1`