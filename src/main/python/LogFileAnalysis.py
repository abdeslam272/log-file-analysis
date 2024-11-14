from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Log File Analysis") \
    .getOrCreate()

# Path to your mounted log file
log_file_path = "/data/raw/Spark_2k.log"

# Read the log file into a DataFrame
logs_df = spark.read.text(log_file_path)

# Show the first few lines of the log file
logs_df.show(10, truncate=False)

# Example: Count occurrences of log levels like ERROR or INFO
error_logs_df = logs_df.filter(logs_df["value"].contains("ERROR"))
info_logs_df = logs_df.filter(logs_df["value"].contains("INFO"))

# Show the counts of ERROR and INFO logs
print(f"ERROR logs count: {error_logs_df.count()}")
print(f"INFO logs count: {info_logs_df.count()}")

# Stop the Spark session
spark.stop()
