import org.apache.spark.SparkContext
import org.apache.spark.SparkConf

object SparkCont {

  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("WordCount").setMaster("local")
    val sc = new SparkContext(conf)
    val rawdata = sc.textFile("C:\\Users\\sayaram\\IdeaProjects\\MyLocal\\src\\main\\scala\\SparkSes.scala")
    val words = rawdata.flatMap(line => line.split(" "))
    val wordCount = words.map(word => (word, 1)).reduceByKey(_ + _)
    wordCount.foreach(println)

  }
}
