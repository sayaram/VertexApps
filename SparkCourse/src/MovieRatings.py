from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("RatingMovie")
sc = SparkContext(conf=conf)
lines = sc.textFile("C:\\git_code\\VertexApps\\SparkCourse\\ml-100k\\u.data")
ratings = lines.map(lambda x: x.split()[2])
result = ratings.countByValue()
sortedResult = collections.OrderedDict(sorted(result.items()))
for key, value in sortedResult.items():
    print("%s %i" % (key, value))



