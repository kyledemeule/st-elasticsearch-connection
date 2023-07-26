# st-elasticsearch

Experimental Connection for Elastic Search in Streamlit.

Note: This uses Elastic Search version `7.10`. There are slight differences in the `elasticsearch` interface in version `8+`.

## Using the Connection

Connect like so:
```
from st_elasticsearch_connection import ElasticSearchConnection

conn = st.experimental_connection("elasticsearch", type=ElasticSearchConnection)
```

Have the `host`, `port`, `access_key`, and `access_secret` in your `secrets.toml` file, or pass them in as arguments to `experimental_connection()`. Then query the connection:

```
test_data = conn.search(index="kibana_sample_data_logs", query={"match_all": {}})
```

## Running Streamlit

Set up a pyenv:

```
pyenv install 3.9
pyenv virtualenv 3.9 stes
pyenv activate stes
pip install -r requirements.txt
```

Then run the app:

```
streamlit run app.py
```

## Setting up ElasticSearch

You can run ES locally, or try a free tier at [bonsai.io](https://bonsai.io/). This project uses the Kibana Sample web logs dataset.
