import streamlit as st
from st_elasticsearch_connection import ElasticSearchConnection

st.title("Elastic Search Experimental Connection")
st.markdown("""
Experimental Connection for Elastic Search
""")

conn = st.experimental_connection("elasticsearch", type=ElasticSearchConnection)
test_data = conn.search(index="kibana_sample_data_logs", query={"match_all": {}})
st.write(test_data)

