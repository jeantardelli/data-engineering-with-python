"""queryusers

This module ilustrates how to query a user using mysql-connector-python
library.
"""
import csv
import mysql.connector

# Create connection to MySQL
db = mysql.connector.connect(option_files='../sql-user/my.ini')
cursor = db.cursor()

# Run the query, selecting only users with age greater than 40
cursor.execute(
    """SELECT *
         FROM dataengineering.people
        WHERE age > %s""", params=(40,))

# Open output file
output = open('fromdb.csv', 'w')
mywriter = csv.writer(output)

# Row Iterator
user = cursor.fetchone()
while user:
    mywriter.writerow(user)
    user = cursor.fetchone()

output.close()
cursor.close()
