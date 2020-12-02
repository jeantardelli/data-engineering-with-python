"""airflowclean

This module ilustrates a cleaning pipeline in Airflow. The following code will
clean data, filter in and write it out to disk.
"""
import datetime as dt
from datetime import timedelta

import pandas as pd

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

def cleanScooter():
    """This functions performs the cleaning taks.

    Firtly, it reads the file and drop unnecessary columns (the region ID).
    Then convert all the columns to lowercase and change the started_at field
    to a datetime data type. Lastly, write the changes to a file.
    """
    df = pd.read_csv('scooter-data/scooter.csv')
    df.drop(columns=['region_id'], inplace=True)
    df.columns = [column.lower() for column in df.columns]
    df['started_at'] = pd.to_datetime(df['started_at'], format='%m/%d/%Y %H:%M')
    df.to_csv('scooter-data/cleanscooter.csv')

def filterData():
    """Reads the cleaned data and filter based on a start and end date."""
    df = pd.read_csv('scooter-data/cleanscooter.csv')
    fromdate = '2019-05-23'
    todate = '2019-06-03'
    tofrom = df[(df['started_at'] > fromdate) & (df['started_at'] < todate)]
    tofrom.to_csv('scooter-data/may23-june3.csv')

default_args = {
    'owner': 'jeantardelli',
    'start_date': dt.datetime(2020, 12, 2),
    'retires': 1,
    'retry_delay': dt.timedelta(minutes=5)
    }

with DAG('CleanData',
         default_args = default_args,
         schedule_interval = timedelta(minutes=5)) as dag:

    cleanData = PythonOperator(task_id='clean',
        python_callable=cleanScooter)
    selectData = PythonOperator(task_id='filter',
        python_callable=filterData)
    copyFile = BashOperator(task_id='copy',
        bash_command='cp ~/data-engineering-with-python/scooter-data/may23-june3.csv ~/may23-june3.csv')

cleanData >> selectData >> copyFile
