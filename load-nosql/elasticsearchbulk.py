"""elasticsearchbulk

This module ilustrates how to add bulks of data to Elasticsearch using Python.
"""
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from faker import Faker

fake = Faker()
es = Elasticsearch()

actions = [
    {
        "_index": "people",
        "_type": "doc",
        "_source": {
            "name": fake.name(),
            "age": fake.random_int(min=18, max=80, step=1),
            "street": fake.street_address(),
            "city": fake.city(),
            "state": fake.state(),
            "zip": fake.zipcode(),
            "lng": fake.longitude(),
            "lat": fake.latitude()
            }
    }
    for _ in range(1000)
]

response = helpers.bulk(es, actions)
print(response)
