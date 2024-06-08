from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Inicialize a sessão do Spark
spark = SparkSession.builder \
    .appName("Exemplo DataFrame Spark") \
    .getOrCreate()

# Defina o esquema do DataFrame
schema = StructType([
    StructField("coluna1", StringType(), True),
    StructField("coluna2", StringType(), True),
    StructField("coluna3", IntegerType(), True),
    StructField("coluna4", IntegerType(), True),
    StructField("coluna5", StringType(), True),
    StructField("coluna6", StringType(), True)
])

# Dados de exemplo para as 20 linhas
dados = [
    ("A", "B", 1, 10, "C", "D"),
    ("E", "F", 2, 20, "G", "H"),
    ("I", "J", 3, 30, "K", "L"),
    ("M", "N", 4, 40, "O", "P"),
    ("Y", "Z", 7, 70, "AA", "BB"),
    ("CC", "DD", 8, 80, "EE", "FF"),
    ("GG", "HH", 9, 90, "II", "JJ"),
    ("KK", "LL", 10, 100, "MM", "NN"),
    ("OO", "PP", 11, 110, "QQ", "RR"),
    ("AAA", "BBB", 14, 140, "CCC", "DDD"),
    ("EEE", "FFF", 15, 150, "GGG", "HHH"),
    ("III", "JJJ", 16, 160, "KKK", "LLL"),
    ("MMM", "NNN", 17, 170, "OOO", "PPP"),
    ("YYY", "ZZZ", 20, 200, "AAA", "BBB")
]

# Crie o DataFrame
df = spark.createDataFrame(dados, schema)

# Exiba o DataFrame
df.show()