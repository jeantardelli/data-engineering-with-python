"""scroll

This module illustrates how to use the scroll, a built-in Elasticsearch method.
"""
from elasticsearch import Elasticsearch

es = Elasticsearch()

res = es.search(
    index = 'people',
    doc_type = 'doc',
    scroll = '20m',
    size = 500,
    body = {"query": {"match_all": {}}})

for search_doc in res['hits']['hits']:
    print(search_doc['_source'])

sid = res['_scroll_id']
size = res['hits']['total']['value']

# Start scrolling
while (size > 0):
    print(size)
    print("-"*25)
    res = es.scroll(scroll_id = sid, scroll='20m')
    sid = res['_scroll_id']
    size = len(res['hits']['hits'])

    for doc in res['hits']['hits']:
        print(doc['_source'])
