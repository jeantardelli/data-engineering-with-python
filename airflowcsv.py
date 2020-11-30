"""airflowcsv

This module ilustrates a data pipeline in Apache Aiflow, using Python and Bash
operators to create tasks that can be combined into a DAG.
"""
import datetime as dt
from datetime import timedelta

import pandas as pd

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

def csvToJson():
    """Reads a CSV file, print out the names and writes it out to JSON"""
    df = pd.read_csv('data.csv')

    for _, row in df.iterrows():
        print(row['name'])

    # Orient records formats the JSON string list like [{column -> value} ...]
    df.to_json('fromAirFlow.json', orient='records')

# Arguments that will be passed to the DAG.
default_args = {
    'owner': 'jeantardelli',
    'start_date': dt.datetime(2020, 11, 30),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5)
    }

# Scheduling a DAG warning
with DAG('MyCSVDAG',
         default_args=default_args,
         schedule_interval=timedelta(minutes=5), # '0 * * * *',
         ) as dag:
    print_starting = BashOperator(task_id='starting',
                        bash_command='echo "I am reading the CSV now..."')
    csvJson = PythonOperator(task_id='convertCSVtoJson',
                        python_callable=csvToJson)

print_starting >> csvJson
