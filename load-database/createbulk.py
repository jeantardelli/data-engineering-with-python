"""createbulk

This module illustrates how to connect to MySQL and load bulk data in python
using the mysql-connector-python library.
"""
import mysql.connector
from faker import Faker

# Create a connection to MySQL
db = mysql.connector.connect(option_files="../sql-user/my.ini")
cursor = db.cursor()

# Create Faker instance
fake = Faker()

# Define the query template and the parameters to submit with it
sql = """INSERT INTO 
             dataengineering.people (name, age, street, city, state, zip, lng, lat)
         VALUES 
             (%(name)s, %(age)s, %(street)s, %(city)s, %(state)s, %(zip)s, %(lng)s, %(lat)s);
      """

params = [
        {'name': fake.name(),
         'age': fake.random_int(min=18, max=80, step=1),
         'street': fake.street_address(),
         'city': fake.city(),
         'state': fake.state(),
         'zip': fake.zipcode(),
         'lng': fake.longitude(),
         'lat': fake.latitude(),
         }
        for _ in range(1000)
        ] 


# Execute queries
cursor.executemany(sql, params)
print("Row count: {0}".format(cursor.rowcount))

db.commit()
db.close()
