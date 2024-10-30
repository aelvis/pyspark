# -*- coding: utf-8 -*-
"""Ejemplo - MAP

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15tnH8QgoIudfBVOCr6k_E5fWYRGhd3Ep
"""

from pyspark.context import SparkContext

sc = SparkContext('local', 'test')

sc2 = SparkContext('local', 'test2')

sc2.stop()

var = sc.parallelize(["b", "a", "c"])

var.map(lambda x: (x, 1)).collect()

var_context = var.map(lambda x: (x, 1))

var_context.collect()

rdd_1 = sc.parallelize([1, 1, 2, 3])

rdd_2 = sc.parallelize([6, 7, 8, 9])

var_general = rdd_1.union(rdd_2)

var_general.collect()

rdd_1.union(rdd_1).collect()

data = sc.parallelize(["python","php","Java"])

data.saveAsTextFile("/content/ejemplo")

nombre = sc.parallelize(["Elvis","Wilson","Raquel"])

nombre.saveAsTextFile("/content/nombre")