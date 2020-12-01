"""eda

This module ilustrates the process of understanding a given dataset. This
process is called exploratory data analysis (EDA). More in-depth analysis
can be done - such as distribution of the data, or the skewness - but these
are not covered here.
"""
import pandas as pd

pd.set_option('display.max_columns', 5)

df = pd.read_csv('scooter.csv')

# Display df columns
print('Dataframe columns:\n'
      '------------------\n'
      '{0}'.format(df.columns))
print('')

# Display df column types
print('Column types:\n'
      '-------------\n'
      '{0}'.format(df.dtypes))
print('')

# Display first 5 (default) entries
print('First entries:\n'
      '--------------\n'
      '{0}'.format(df.head()))
print('')

# Display a specific df column (DURATION)
print('DURATION column:\n'
      '----------------\n'
      '{0}'.format(df['DURATION']))
print('')

# Display a list of columns
print('trip_id, DURATION and, start_location_name columns:\n'
      '---------------------------------------------------\n'
      '{0}'.format(df[['trip_id', 'DURATION', 'start_location_name']]))
print('')

# Pull a sample from the data
print('Sample of 5 (random) ids:\n'
      '-------------------------\n'
      '{0}'.format(df.sample(5)))
print('')

# Slices
print('Slicing df (first ten):\n'
      '-----------------------\n'
      '{0}'.format(df[:10]))
print('')

# Locate by index
print('Locate index 34221:\n'
      '-------------------\n'
      '{0}'.format(df.loc[34221]))
print('')

# Selecting single values
print('Select index 2, column "DURATION":\n'
      '----------------------------------\n'
      '{0}'.format(df.at[2, 'DURATION']))
print('')

# Select rows based on conditions
print('Select rows where user_id equals 8417864:\n'
      '-----------------------------------------\n'
      '{0}'.format(df.where(df['user_id'] == 8417864)))
print('')

# Use where and condition passing
one = df['user_id'] == 8417864
two = df['trip_ledger_id'] == 1488838
print('Select user_id 8417864 and trip_ldger_id 1488838:\n'
      '-------------------------------------------------\n'
      '{0}'.format(df.where(one & two)))
print('')
print('{0}'.format(df[(one)&(two)]))
print('')

# Summary Statistics
print('Summary statistics:\n'
      '-------------------\n'
      '{0}'.format(df.describe()))
print('')

# Summary Statistics of a single column
print('start_location_name summary statistics:\n'
      '---------------------------------------\n'
      '{0}'.format(df['start_location_name'].describe()))
print('')

# Counts for all unique values
print('Value and count for all unique values:\n'
      '--------------------------------------\n'
      '{0}'.format(df['DURATION'].value_counts()))
print('')

# Counts for all unique values percentage (normalized)
print('Percentage:\n'
      '-----------\n'
      '{0}'.format(df['DURATION'].value_counts(normalize=True)))
print('')

# Counting missing values
print('end_location_name missing values:\n'
      '---------------------------------\n'
      '{0}'.format(df['end_location_name'].value_counts(dropna=False)))
print('')

# Count missing values of all columns
print('Missing values:\n'
      '---------------\n'
      '{0}'.format(df.isnull().sum()))
print('')

# Count values in bins
print('trip_id bins of 10:\n'
      '-------------------\n'
      '{0}'.format(df['trip_id'].value_counts(bins=10)))
print('')
