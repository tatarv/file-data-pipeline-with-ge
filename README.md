# file-data-pipeline
This repo aims to validate a file ingestion into a full and real data pipeline for Data Engineers


## Start Airflow Service

Enter into airflow sub directory
```sh
$ cd airflow
```

Prepare .env file for airflow
```sh
$ mv .env-default .env
```

Build the customized image for airflow
```sh
$ make build
```

Load the initial configurations (This command is necessary only once)
```sh
$ make airflow-init
```

Start all docker containers for airflow
```sh
$ make up
```

Access the host in your browser and use the credentials below:
```
host: http://localhost:8080/home
user: airflow
password: airflow
```

Important for execute Spark Jobs.

Configure the Spark connection: In Airflow, go to Admin -> Connections and add a new connection. Set the Conn Id as spark_default, the Conn Type as Spark, and the Host as the address of your Spark master.
```
Connection Id: spark_default
Connection Type: Spark
Host: spark://spark-master:7077
```