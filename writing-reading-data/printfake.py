"""loadcsv

This module contains the code that prints lots of data using the faker library.
"""
from faker import Faker

fake = Faker()
header = ['name', 'age', 'street', 'city', 'state', 'zip', 'lng', 'lat']

print(','.join(header))
for _ in range(1000):
    record = [
        fake.name(), fake.random_int(min=18, max=80, step=1),
        fake.street_address(), fake.city(), fake.state(),
        fake.zipcode(),fake.longitude(), fake.latitude()
    ]
    record = [str(r) for r in record]
    print(','.join(record))
