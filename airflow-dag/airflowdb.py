"""airflowdb

This module illustrates a DAG that queries MySQL database, save it as a CSV
file and the read it and write it to an Elasticsearch index.

This DAG is composed of only two - atomic - tasks.
"""
import datetime as dt
import pandas as pd
import mysql.connector

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

from elasticsearch import Elasticsearch

def queryMySQL():
    """Query MySQL database and write the results

    This funtion creates a connection with MySQL using mysql.connector,
    execute the sql query using pandas.read_sql() method and then use
    pandas.to_csv() to write data to disk."""
    db = mysql.connector.connect(option_files='../sql-user/my.ini')
    df = pd.read_sql("SELECT name, city FROM dataengineering.people", db)
    df.to_csv('mysqldata.csv')
    print("--------Data Saved---------")

def insertElasticsearch():
    """Inserts data into Elasticsearch

    This function creates an Elasticsearch object connected to localhost. Then,
    read the CSV file with pandas from the queryMySQL method, iterating through
    it and converting each row into JSON format. Finally, it creates an index
    in the Elasticsearch.
    """
    es = Elasticsearch()
    df = pd.read_csv('mysqldata.csv')

    for _, row in df.iterrows():
        doc = row.to_json()
        res = es.index(index='frommysql', doc_type='doc', body=doc)
        print(res)

# Specify the arguments for the DAG.
default_args = {
    'owner': 'jeantardelli',
    'start_date': dt.datetime(2020, 12, 1),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5)
    }

# Pass the arguments to the DAG, name it and set the run interval.
with DAG('MyDbDAG',
         default_args=default_args,
         schedule_interval='@once', # Will run just once
         ) as dag:

    print_starting = BashOperator(task_id='Starting',
        bash_command='echo "I am querying MySQL now...."')
    getData = PythonOperator(task_id='QueryMySQL',
        python_callable=queryMySQL)
    print_inserting = BashOperator(task_id='InsertElastic',
        bash_command='echo "I am inserting data into Elasticsearch now...."')
    insertData = PythonOperator(task_id='InsertDataElasticsearch',
        python_callable=insertElasticsearch)

print_starting >> getData >> print_inserting >> insertData
