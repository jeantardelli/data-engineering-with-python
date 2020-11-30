"""readjson

This module contains code that reads a json file using the standard json library.
"""
import json

with open('data.json') as f:
    data = json.load(f)

print(type(data))
print(data['records'][0]['name'])
