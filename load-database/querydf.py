"""querydf

This module ilustrates how to query a MySQL database using a DataFrame object.
"""
import mysql.connector
import pandas as pd

# Create connection to MySQL
db = mysql.connector.connect(option_files='../sql-user/my.ini')

# Execute a query in a DataFrame using a built-in method and
# print the first 5 elements
df = pd.read_sql("SELECT * FROM dataengineering.people", db)
print(df.head())

# Export it to a JSON file
df.to_json('fromdb.json', orient='records')
