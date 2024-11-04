# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SgZcguxsBY0BWpdQFYPeXoniVrfT-QG-
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, mean, expr, corr

spark = SparkSession.builder.appName("Estadísticas").getOrCreate()

data = [("Juan", 23), ("María", 22), ("Ana", 24), ("Luis", 24), ("Pedro", 23), ("Miguel", 22), ("Carlos", 23), ("Laura", 22)]
columns = ["Nombre", "Edad"]
df = spark.createDataFrame(data, columns)

media = df.select(mean(col("Edad")).alias("Media")).collect()

percentiles = df.approxQuantile("Edad", [0.5], 0.0)
mediana = percentiles

moda = df.groupBy("Edad").count().orderBy("count", ascending=False).first()["Edad"]

print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

data = [("A", 1, 2.0), ("B", 2, 3.0), ("C", 3, 4.0), ("D", 4, 5.0), ("E", 5, 6.0)]

data_2 = [("A", 1, 3), ("B", 2, 2), ("C", 3, 1), ("D", 2, 2), ("E", 3, 3), ("F", 1, 2), ("G", 2, 1), ("H", 3, 2), ("I", 1, 3), ("J", 2, 2), ("K",3, 1)]

schema = ["id", "variable1", "variable2"]

df = spark.createDataFrame(data_2, schema)

correlation = df.select(corr("variable1", "variable2").alias("correlation")).collect()[0]["correlation"]

print(f"Correlación entre variable1 y variable2: {correlation}")