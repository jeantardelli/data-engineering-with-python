"""createrecords

This module ilustrates how to connect to MySQL and create a record in python
using the mysql-connector-python library.
"""
import mysql.connector

# Create a connection to MySQL
db = mysql.connector.connect(option_files="../sql-user/my.ini")
cursor = db.cursor()

# Define the query template and the parameters to submit with it
sql = """INSERT INTO 
             dataengineering.people (name, age, street, city, state, zip, lng, lat)
         VALUES 
             (%(name)s, %(age)s, %(street)s, %(city)s, %(state)s, %(zip)s, %(lng)s, %(lat)s);
      """

params = (
    {
        'name': 'Robin Hill',
        'age': 58,
        'street': '256 Diane Mission',
        'city': 'Langton',
        'state': 'Iowa',
        'zip': '57920',
        'lng': 89.438553,
        'lat': -11.544307,
    },
    {
        'name': 'Parker Stone',
        'age': 67,
        'street': '2143 Nunez Isle',
        'city': 'Shellyborough',
        'state': 'Delaware',
        'zip': '11567',
        'lng': 26.731914,
        'lat': 48.7766565,
    }
)


# Execute queries
cursor.executemany(sql, params)
print("Row count: {0}".format(cursor.rowcount))
print("Last statement: {0}".format(cursor.statement))

db.commit()
db.close()
