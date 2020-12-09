"""loadjson-datalake

This module contains the code that writes lots of data using the faker library.
It simulates how files in a datalake would be like.
"""
import json
import os
from faker import Faker

os.chdir("../datalake")

fake = Faker()
userid = 1

for _ in range(1000):
    name = fake.name()
    filename = name.replace(" ", "-") + ".json"

    data = {'userid': userid,
            'name': name,
            'age': fake.random_int(min=18, max=101, step=1),
            'street': fake.street_address(),
            'city': fake.city(),
            'state': fake.state(),
            'zip': fake.zipcode(),
            'lng': float(fake.longitude()),
            'lat': float(fake.latitude())
            }

    datajson = json.dumps(data)
    output = open(filename, 'w')
    output.write(datajson)
    output.close()

    userid += 1
