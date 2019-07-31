from pyspark import SparkConf, SparkContext
from operator import add

conf = SparkConf().setAppName("Test").setMaster("local")
sc = SparkContext(conf=conf)
words = sc.parallelize (["This is Sayaram Gattu", "Jesus is my God"]).flatMap(lambda line: line.split(' '))
count = words.map(lambda x: (x, 1)).reduceByKey(add).collect()

for (word, count) in count:
    print(word, count)





