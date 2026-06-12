from pyspark.sql import SparkSession

spark = SparkSession.builder.master('local[4]').getOrCreate()
df = spark.read.parquet('large_dataset.parquet')

# Distributed processing
result = df.groupBy('group').agg({'value': 'mean'})
result.write.parquet('output/')