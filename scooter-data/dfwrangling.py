"""dfwrangling

This module ilustrates some common data modification using pandas.
"""
import pandas as pd

df = pd.read_csv('scooter.csv')

print("Df columns:\n"
      "-----------\n"
      "{0}".format(df.columns))
print("")

# renaming just one (or more) columns
df.rename(columns = {'DURATION': 'duration', 'region_id': 'region'}, inplace=True)
print("Df columns:\n"
      "-----------\n"
      "{0}".format(df.columns))
print("")

# normalizing column names
df.columns = [col.upper() for col in df.columns]
print("Df columns:\n"
      "-----------\n"
      "{0}".format(df.columns))
print("")

# Modifying columns
df['MONTH'] = df['MONTH'].str.upper()
print("Column MONTH:\n"
      "-------------\n"
      "{0}".format(df["MONTH"].head()))
print("")

# Efficiently change a specific dataframe value
df.loc[df["TRIP_ID"] == 1613335, "NEW_COLUMN"] = '1613335'
values = {"NEW_COLUMN": "No"}
df.fillna(value=values, inplace=True)

print("TRIP_ID and NEW COLUMN:\n"
      "-----------------------\n"
      "{0}".format(df[["TRIP_ID", "NEW_COLUMN"]].head()))
print("")

# Split text
d = df[["TRIP_ID", "STARTED_AT"]].head()
d["STARTED_AT"] = d["STARTED_AT"].str.split()
print("Split Text:\n"
      "-----------\n"
      "{0}".format(d))
print("")

# Expanding text
new = df["STARTED_AT"].head().str.split(expand=True)
print("Expanding columns (str.split):\n"
      "------------------------------\n"
      "{0}".format(new))
print("")

d["DATE"] = new[0]
d["TIME"] = new[1]
print("Passing to another data frame:\n"
      "------------------------------\n"
      "{0}".format(d))
print("")

# Mofifying column type
d = df[["TRIP_ID", "STARTED_AT"]].head()
d["STARTED_AT"] = pd.to_datetime(df["STARTED_AT"], format='%m/%d/%Y %H:%M')
print("Dataframe columns' types:\n"
      "-------------------------\n"
      "{0}".format(d.dtypes))
