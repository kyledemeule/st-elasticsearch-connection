from streamlit.connections import ExperimentalBaseConnection
from streamlit.runtime.caching import cache_data

import elasticsearch

class ElasticSearchConnection(ExperimentalBaseConnection[elasticsearch.Elasticsearch]):
  """Basic st.experimental_connection implementation for ElasticSearch"""

  def _connect(self, **kwargs) -> elasticsearch.Elasticsearch:
    if "host" in kwargs:
      host = kwargs.pop("host")
    else:
      host = self._secrets["host"]

    if "port" in kwargs:
      port = kwargs.pop("port")
    else:
      port = self._secrets["port"]

    if "access_key" in kwargs:
      access_key = kwargs.pop("access_key")
    else:
      access_key = self._secrets["access_key"]

    if "access_secret" in kwargs:
      access_secret = kwargs.pop("access_secret")
    else:
      access_secret = self._secrets["access_secret"]

    elasticsearch_access = "https://{access_key}:{access_secret}@{host}:{port}".format(
      host=host,
      port=port,
      access_key=access_key,
      access_secret=access_secret
    )
    es = elasticsearch.Elasticsearch(
      hosts=elasticsearch_access
    )

    return es

  def search(self, index: str, query: dict, ttl: int = 3600, **kwargs) -> dict:
    @cache_data(ttl=ttl)
    def _search(index: str, query: str, **kwargs) -> dict:
        response = self._instance.search(index=index, body={"query": query})
        return response

    return _search(index, query, **kwargs)

