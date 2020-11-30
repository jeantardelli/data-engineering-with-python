## Data Engineering w/ Python

This repo contains the source code for data engineering with Python.

## Tools

Following is the list of the tools that will be used:

* Programming Language: Python
* SQL Database: MySQL
* NoSQL Database: Elasticsearch + Kibana
* Data Processing Engine: Apache Spark
* Data Pipelines: Apache Airflow, Apache NiFi

## Directories

* writing-reading-data: this directory contains modules that create and read fake data
* sql-user: this directory contains the query to create a user and its credentials data
* load-database: this directory contains modules that load and query data from MySQL
* load-nosql: this directory contains modules that load and query data from Elasticsearch

## Setup working environment

To setup the working environment run the command:

```bash
$ source start-working-environment
```

If you want to stop/kill the working environment, run the command:

```bash
$ ./stop-working-environment
```

## License
[MIT](LICENSE)
