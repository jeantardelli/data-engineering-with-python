## Data Engineering w/ Python

This repo contains the source code for data engineering with Python.

## Software and Hardware List

| Software required                                                                               | OS used        |
| ------------------------------------------------------------------------------------------------|----------------|
|   Python 3.x, Spark 3.x, Nifi 1.x, MySQL 8.0.x, Elasticsearch 7.x, Kibana 7.x, Apache Kafka 2.x | Linux (Ubuntu) |

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
