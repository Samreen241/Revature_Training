import os
import sys
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim, lower, coalesce, lit, to_date, year

# ================================
# 1. Set environment variables
# ================================
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17"
os.environ["SPARK_HOME"] = r"C:\RevatureInternshipTraining\Project1_Media_Content\content\.venv\Lib\site-packages\pyspark"
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# ================================
# 2. Start Spark session
# ================================
spark = SparkSession.builder.appName("StreamingContentCleaning").getOrCreate()

# ================================
# 3. Load datasets
# ================================
df_netflix = spark.read.csv(
    r"C:\RevatureInternshipTraining\Project1_Media_Content\content\data\netflix_titles.csv",
    header=True, inferSchema=True
)

df_disney = spark.read.csv(
    r"C:\RevatureInternshipTraining\Project1_Media_Content\content\data\disney_plus_titles.csv",
    header=True, inferSchema=True
)

# ================================
# 4. Basic cleaning with PySpark
# ================================
def clean_spark_df(df):
    df = df.dropDuplicates().na.drop(subset=["title", "type"])  # drop rows with missing title/type
    df = df.withColumn("title", trim(lower(col("title"))))
    df = df.withColumn("type", trim(lower(col("type"))))
    # Fill missing country and rating in Spark
    df = df.withColumn("country", coalesce(col("country"), lit("Unknown")))
    df = df.withColumn("rating", coalesce(col("rating"), lit("Not Rated")))
    # Convert date_added to proper date and extract year/month
    df = df.withColumn("date_added", to_date(col("date_added"), "MMMM d, yyyy"))
    df = df.withColumn("year_added", year(col("date_added")))
    return df

df_netflix_clean = clean_spark_df(df_netflix)
df_disney_clean = clean_spark_df(df_disney)

# ================================
# 5. Convert to Pandas for advanced processing
# ================================
df_netflix_pd = df_netflix_clean.toPandas()
df_disney_pd = df_disney_clean.toPandas()

# ================================
# 6. Add platform labels
# ================================
df_netflix_pd["platform"] = "Netflix"
df_disney_pd["platform"] = "Disney"

# ================================
# 7. Merge datasets
# ================================
df_combined = pd.concat([df_netflix_pd, df_disney_pd], ignore_index=True)

# ================================
# 8. Handle release_year and content_age
# ================================
df_combined["release_year"] = pd.to_numeric(df_combined["release_year"], errors="coerce").fillna(2020)
df_combined["content_age"] = 2025 - df_combined["release_year"]

# ================================
# 9. Save cleaned dataset to output folder
# ================================
output_data_dir = os.path.join(os.getcwd(), "output", "data")
os.makedirs(output_data_dir, exist_ok=True)
output_file = os.path.join(output_data_dir, "cleaned_streaming_titles.csv")
df_combined.to_csv(output_file, index=False)

print(f"✔ Cleaned dataset saved successfully at {output_file}\n")

# ================================
# 10. Quick summary
# ================================
print(df_combined.info())
print(df_combined.describe())
print(df_combined["platform"].value_counts())
