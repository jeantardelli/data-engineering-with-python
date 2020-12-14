[![Issues](https://img.shields.io/github/issues/jeantardelli/data-engineering-with-python)](https://github.com/jeantardelli/data-engineering-with-python/issues)
[![Forks](https://img.shields.io/github/forks/jeantardelli/data-engineering-with-python)]()
[![Stars](https://img.shields.io/github/stars/jeantardelli/data-engineering-with-python)]()
[![MIT License](https://img.shields.io/github/license/jeantardelli/data-engineering-with-python)](LICENSE)

## Data Engineering w/ Python

This repo contains the source code for data engineering with Python.

## Software and Hardware List

| Software required                                                                               | OS used            |
| ------------------------------------------------------------------------------------------------|--------------------|
|   Python 3.x, Spark 3.x, Nifi 1.x, MySQL 8.0.x, Elasticsearch 7.x, Kibana 7.x, Apache Kafka 2.x | Linux (any distro) |

## Directories

* airflow-dag: this directory contains the airflow DAG modules used in this repo
* great_expectations: contains all the important components of a local Great Expectation deployment
* kafka-producer-consumer: contains modules that produce and consume Kafka topics in Python
* load-database: this directory contains modules that load and query data from MySQL
* load-nosql: this directory contains modules that load and query data from Elasticsearch
* nifi-datalake: this directory contains Nifi Pipelines to simulate reading data from the datalike
* nifi-files: this directory contains the files derived from the Nifi template pipelines
* nifi-scanfiles: this directory contains dictionary files read by ScanContent processor (e.g. VIP)
* nifi-scripts: this directory contains shell scripts that are used with ExecuteStreamCommand in Nifi
* nifi-templates: this directory contains different Apache Nifi pipeline templates
* nifi-versioning: this directory contains Nifi pipelines with version control (NiFi Regsitry)
* scooter-data: this directory contains the scooter dataset and wrangling data modules (pandas)
* sql-user: this directory contains the query to create a user and its credentials data
* writing-reading-data: this directory contains modules that create and read fake data

## Setup working environment

To setup the working environment run the command:

```bash
$ source start-working-environment
```

If you want to stop/kill the working environment, run the command:

```bash
$ ./stop-working-environment
```

## Creating DB user

To create the MySQL user, run the following statement as the root user:

```bash
$ mysql -u root -p -e "SOURCE sql-user/create-user.sql"
```
This will also grant access to the databases used in this repo.

## License
[MIT](LICENSE)
