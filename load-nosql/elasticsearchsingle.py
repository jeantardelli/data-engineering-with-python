"""elasticsearchsingle

This module ilustrates how to load data into Elastisearch database, a NoSQL
columnar storage tool.
"""
from elasticsearch import Elasticsearch
from faker import Faker

fake = Faker()
es = Elasticsearch() # or ip {N.N.N.H}

doc = {"name": fake.name(),
       "age": fake.random_int(min=18, max=80, step=1),
       "street": fake.street_address(),
       "city": fake.city(),
       "state": fake.state(),
       "zip": fake.zipcode(),
       "lng": fake.longitude(),
       "lat": fake.latitude()
       }

# Add data to Elasticsearch
res = es.index(index="people", doc_type="doc", body=doc)
print(res)
