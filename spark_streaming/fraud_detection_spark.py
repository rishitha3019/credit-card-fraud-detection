from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import joblib
import pandas as pd

spark = SparkSession.builder.appName("FraudDetection").getOrCreate()
df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "credit-transactions") \
    .load()

df = df.selectExpr("CAST(value AS STRING)")
# Add your logic here to deserialize JSON, apply XGBoost model, and save frauds to PostgreSQL
