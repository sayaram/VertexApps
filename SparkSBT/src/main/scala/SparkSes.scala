import org.apache.spark.sql.SparkSession

object SparkSes {

  def main(args: Array[String]) {

    val sparkSession = SparkSession.builder
      .master("local")
      .appName("spark session example")
      .getOrCreate()

    val df = sparkSession.read
      .option("header", "true")
      .csv("src/main/resources/sales.csv")
    df.show()

  }
}
