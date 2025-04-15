import sys
from pyspark.context import SparkContext
from pyspark.sql.functions import col, when
from pyspark.sql.types import DoubleType
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from awsglue.job import Job

# Initialize Glue
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# --- Extract ---
input_path = "s3://arn:aws:s3:::<your-s3-bucket>//raw/Fashion_Retail_Sales.csv"
df = spark.read.option("header", True).csv(input_path)

# --- Transform ---
# Convert numeric columns to appropriate types
df = df.withColumn("Purchase Amount (USD)", col("Purchase Amount (USD)").cast(DoubleType()))
df = df.withColumn("Review Rating", col("Review Rating").cast(DoubleType()))

# Fill missing Review Rating with average
avg_rating = df.selectExpr("avg(`Review Rating`) as avg").collect()[0]['avg']
df = df.withColumn("Review Rating", when(col("Review Rating").isNull(), avg_rating).otherwise(col("Review Rating")))

# Filter rows where Purchase Amount > 3000
df = df.filter(col("Purchase Amount (USD)") > 3000)

# --- Load ---
output_path = "s3://arn:aws:s3:::<your-s3-bucket>//processed/"
df.write.mode("overwrite").option("header", True).csv(output_path)

job.commit()
