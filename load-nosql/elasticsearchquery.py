"""elasticsearchquery

This module ilustrates how to query Elasticsearch with Python.
"""
import pandas as pd
from elasticsearch import Elasticsearch

es = Elasticsearch()

# Get all the documents
doc = {"query": {"match_all": {}}}
res = es.search(index="people", body=doc, size=10)
print(res['hits']['hits'][9]['_source'])

# Get Tina Solis
doc = {"query": {"match": {"name": "Tina Solis"}}}
res = es.search(index="people", body=doc, size=10)
print(res['hits']['hits'][0]['_source'])

# Get Tina using Lucene syntax
res = es.search(index="people", q="name:Tina Solis", size=10)
print(res['hits']['hits'][0]['_source'])

# Get city South Robert using pandas
doc = {"query": {"match": {"city": "South Robert"}}}
res = es.search(index="people", body=doc, size=10)
df = pd.json_normalize(res['hits']['hits'])
print(df.head())

# Get Illinois state and filter on zip
doc = {"query":
        {"bool":
            {"must":
                {"match": {"state": "Illinois"}},
                "filter": {"term": {"zip": "30990"}}
        }}}

res = es.search(index="people", body=doc, size=10)
print(res['hits']['hits'][0]['_source'])
