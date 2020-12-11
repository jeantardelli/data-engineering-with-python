"""
kproducer

This module illustrates how to create a Kafka producer using Python.
"""
import json
import time

from confluent_kafka import Producer
from faker import Faker

fake = Faker()
p = Producer({'bootstrap.servers': 'localhost:9092,localhost:9093,localhost:9094'})

def receipt(err, msg):
    """Defines an acknowledgments for the producer and consumer"""
    if err is not None:
        print("Error: {0}".format(err))
    else:
        print("{0}: Message on topic {1} on partition {2} with a value"
              " of {3}".format(
                  time.strftime(
                      '%Y-%m%d %H:%M:%S',
                      time.localtime(msg.timestamp()[1]/1000)),
                  msg.topic(),
                  msg.partition(),
                  msg.value().decode('utf-8')))

print("Topics available to publish: {0}".format(', '.join(p.list_topics().topics)))

for _ in range(10):

    data = {'name': fake.name(),
            'age': fake.random_int(min=18, max=101, step=1),
            'street': fake.street_address(),
            'city': fake.city(),
            'state': fake.state(),
            'zip': fake.zipcode(),
            'lng': float(fake.longitude()),
            'lat': float(fake.latitude())
            }

    m = json.dumps(data)
    p.poll(0)
    p.produce('users', m.encode('utf-8'), callback=receipt)

p.flush()
