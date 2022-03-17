"""
conding = utf-8
@Author : Wu Wentong
@Time   : 2022/3/17 上午10:42
@Site   : 
@File   : pysparktest.py
@SoftWare: PyCharm
"""
from pyspark import SparkContext

sc = SparkContext("local", "count app")
words = sc.parallelize(
    ["scala",
     "java",
     "hadoop",
     "spark",
     "akka",
     "spark vs hadoop",
     "pyspark",
     "pyspark and spark"
     ])
counts = words.count()
print("Number of elements in RDD -> %i" % counts)
