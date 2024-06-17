from delta.tables import DeltaTable
from pyspark.sql import SparkSession
from pyspark.sql.functions import col


def merge_delta(delta_table, new_data, merge_key):
    (
        delta_table.alias("old_data")
            .merge(
                new_data.alias("new_data"),
                f"old_data.{merge_key} = new_data.{merge_key}"
            )
            .whenMatchedUpdate(set = {
                "first_name": col("new_data.first_name"),
                "total": col("new_data.total")
            })
            .whenNotMatchedInsert(values = {
                "first_name": col("new_data.first_name"),
                "total": col("new_data.total")
            })
            .execute()
    )

    return delta_table


def create_delta(new_data, delta_path, schema, table):
    (
        new_data.write.format("delta")
            .option("delta.columnMapping.mode", "name")
            .option("path", delta_path)
            .saveAsTable(f"{schema}.{table}")
    )


def main():
    source_bucket = None
    target_bucket = "datalake"
    schema = "datalake"
    table = "agg_table"
    primary_key = "first_name"

    agg_query = """
    WITH splitted_names as (
        SELECT 
            split(name, ' ')[0] as first_name, 
            split(name, ' ')[1] as last_name
        FROM datalake.test_table
    )

    SELECT 
    first_name, count(1) total
    FROM splitted_names
    GROUP BY first_name
    ORDER BY total desc
    ;
    """

    spark = SparkSession.builder \
        .appName("Create Agg Delta Table") \
        .enableHiveSupport() \
        .getOrCreate()

    delta_path = f"s3a://{target_bucket}/delta/datalake/tables/{table}"

    new_data = spark.sql(agg_query)
    new_data.show(10)

    spark.sql(f"CREATE DATABASE IF NOT EXISTS {schema}")
    spark.sql(f"USE {schema}")

    try:
        delta_table = DeltaTable.forPath(spark, delta_path)
        delta_table = merge_delta(delta_table, new_data, primary_key)
    except:
        create_delta(new_data, delta_path, schema, table)
        delta_table = DeltaTable.forName(spark, f"{schema}.{table}")

    delta_table.toDF().show(10)


if __name__ == "__main__":
    main()