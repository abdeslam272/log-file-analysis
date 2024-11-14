import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._ // Import necessary functions

val spark = SparkSession.builder()
  .appName("Log File Analysis")
  .getOrCreate()

// Reading the log file into a DataFrame
val logDF = spark.read.text("/data/raw/Spark_2k.log")

// Filtering for logs containing the string "ERROR"
val errorLogs = logDF.filter($"value".contains("ERROR"))

// Counting error log occurrences
val errorCount = errorLogs.groupBy("value").count()

// Showing the results
errorCount.show()
