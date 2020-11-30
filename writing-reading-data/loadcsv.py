"""loadcsv

This module contains the code that writes lots of data using the faker library.
"""
import csv
from faker import Faker

output = open('/../data.csv', 'w')
fake = Faker()
header = ['name', 'age', 'street', 'city', 'state', 'zip', 'lng', 'lat']

mywriter = csv.writer(output)
mywriter.writerow(header)

for _ in range(1000):
    mywriter.writerow(
            [fake.name(), fake.random_int(min=18, max=80, step=1),
             fake.street_address(), fake.city(), fake.state(),
             fake.zipcode(),fake.longitude(), fake.latitude()]
            )

output.close()
