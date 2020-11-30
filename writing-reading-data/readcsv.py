"""readcsv

This module contains code that reads a csv file using the standard csv library.
"""
import csv
import os

with open('/../data.csv') as f:
    myreader = csv.DictReader(f)
    headers = next(myreader)

    for row in myreader:
        print(row['name'])
