"""dfenriching

This module ilustrate examples that enrich a dataset using pandas.
"""
import pandas as pd

df = pd.read_csv('scooter.csv')

# Take a subset of the data
new = pd.DataFrame(df['start_location_name'].value_counts().head())
new.reset_index(inplace=True)
new.columns=['address', 'count']

print("First entries:\n"
      "--------------\n"
      "{0}".format(new))
print("")

# Collect only the street address (necessary to geocode)
# It also replaces the '@' with the word 'and'
n = new['address'].str.split(pat=',', n=1, expand=True)
replaced = n[0].str.replace("@", "and")

new['street'] = replaced
print("Adding a well formated 'street' column:\n"
      "---------------------------------------\n"
      "{0}".format(new))
print("")

# Enriching the dataset combining with other resources (geocodestreet.csv file)
geo = pd.read_csv('geocodestreet.csv')
print("Geocoded streets:\n"
      "-----------------\n"
      "{0}".format(geo))
print("")

# Joining dataframes
joined = new.join(other=geo, how='left', lsuffix='_new', rsuffix='_geo')
print("Joined Dataframes:\n"
      "------------------\n"
      "{0}".format(joined[['street_new', 'street_geo', 'x', 'y']]))
print("")

# Merge dataframes (does not generate duplicates)
merge = pd.merge(new, geo, on='street')
print("Merge Dataframe columns:\n"
      "------------------------\n"
      "{0}".format(merge.columns))
