from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from influxdb import InfluxDBClient


#  SPARK SESSION

spark = SparkSession.builder \
    .appName("WeatherStreamFixed") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")


# KAFKA STREAM

df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "myweather") \
    .option("startingOffsets", "latest") \
    .load()

json_df = df.selectExpr("CAST(value AS STRING) as json_str")


#  EXACT SCHEMA FOR YOUR DATA

schema = StructType([
    StructField("timestamp", StringType()),
    StructField("location", StringType()),
    StructField("source", StringType()),
    StructField("weather", StructType([
        StructField("time", StringType()),
        StructField("interval", IntegerType()),
        StructField("temperature", DoubleType()),
        StructField("windspeed", DoubleType()),
        StructField("winddirection", IntegerType()),
        StructField("is_day", IntegerType()),
        StructField("weathercode", IntegerType())
    ]))
])

parsed = json_df.select(from_json(col("json_str"), schema).alias("data")).select("data.*")


#  INFLUXDB WRITER

def write_to_influx(batch_df, batch_id):
    client = InfluxDBClient(host='localhost', port=8086)
    client.switch_database('weatherdb')

    rows = batch_df.collect()

    points = []

    for r in rows:
        try:
            points.append({
                "measurement": "weather",
                "tags": {
                    "location": r.location
                },
                "time": r.timestamp,
                "fields": {
                    "temperature": float(r.weather["temperature"]),
                    "windspeed": float(r.weather["windspeed"]),
                    "winddirection": int(r.weather["winddirection"]),
                    "is_day": int(r.weather["is_day"]),
                    "weathercode": int(r.weather["weathercode"])
                }
            })
        except Exception as e:
            print("Bad row skipped:", e)

    if points:
        client.write_points(points)
        print(f"Inserted {len(points)} points")


# START STREAM

query = parsed.writeStream \
    .foreachBatch(write_to_influx) \
    .outputMode("append") \
    .start()

query.awaitTermination()