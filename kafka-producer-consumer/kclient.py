"""
kclient

This module illustrates how to create a Kafka consumer in Python
"""
from confluent_kafka import Consumer

c = Consumer({
    'bootstrap.servers': 'localhost:9092,localhost:9093,localhost:9094',
    'group.id': 'python-consumer',
    'auto.offset.reset': 'earliest'
    })

t = c.list_topics()
print("Topics available to consume: {0}".format(', '.join(t.topics)))
print("# of partitions for topic 'users': {0}".format(
    t.topics['users'].partitions))

# Subscribe to a particular topic
c.subscribe(['users'])

while True:
    msg = c.poll(1.0) # timeout

    if msg is None:
        continue

    if msg.error():
        print("Error: {0}".format(msg.error()))
        continue

    data = msg.value().decode('utf-8')
    print(data)

c.close()
