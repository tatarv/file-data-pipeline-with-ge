from delta.tables import DeltaTable
from pyspark.sql import SparkSession

def main():

    source_bucket = "datalake-landing"
    target_bucket = "datalake"

    spark = SparkSession.builder \
        .appName("CSV File to Delta Lake Table") \
        .enableHiveSupport() \
        .getOrCreate()

    input_path = f"s3a://{source_bucket}/*.csv"
    delta_path = f"s3a://{target_bucket}/delta/datalake/tables/"

    spark.sql("DROP SCHEMA IF EXISTS datalake CASCADE")

    spark.sql("CREATE DATABASE IF NOT EXISTS datalake")
    spark.sql("USE datalake")

    df = spark.read.csv(input_path, header=True, inferSchema=True)

    df.show()

    df.write.format("delta").option("delta.columnMapping.mode", "name")\
        .option("path", f'{delta_path}/test_table')\
        .saveAsTable("datalake.test_table")

    dt = DeltaTable.forName(spark, "datalake.test_table")

    dt.toDF().show()


if __name__ == "__main__":
    main()