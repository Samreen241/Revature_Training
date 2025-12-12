import sys
import os
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_replace, to_date, lit

# =========================================
# ENVIRONMENT SETUP FOR PYSPARK
# =========================================

import findspark
findspark.init("C:/spark")

# os.environ["JAVA_HOME"] = "C:/Program Files/Java/jdk-21"
# os.environ["SPARK_HOME"] = "C:/RevatureInternshipTraining/Media_Content/.venv/Lib/site-packages/pyspark"
# os.environ["PYSPARK_PYTHON"] = sys.executable
# os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

# =========================================
# STEP 1: LOAD DATA USING PANDAS
# =========================================
disney = pd.read_csv("../Data_Resources/disney_plus_titles.csv")
netflix = pd.read_csv("../Data_Resources/netflix_titles.csv")

# =========================================
# STEP 2: CLEAN USING PANDAS
# =========================================
disney_cleaned_pd = disney.dropna().reset_index(drop=True)
netflix_cleaned_pd = netflix.dropna().reset_index(drop=True)

# Standardize column names
disney_cleaned_pd.columns = disney_cleaned_pd.columns.str.strip().str.lower().str.replace(" ", "_")
netflix_cleaned_pd.columns = netflix_cleaned_pd.columns.str.strip().str.lower().str.replace(" ", "_")

# Rename
disney_cleaned_pd.rename(columns={'listed_in': 'genre'}, inplace=True)
netflix_cleaned_pd.rename(columns={'listed_in': 'genre'}, inplace=True)

# Standardize dates
disney_cleaned_pd["date_added"] = pd.to_datetime(disney_cleaned_pd["date_added"], errors="coerce")
netflix_cleaned_pd["date_added"] = pd.to_datetime(netflix_cleaned_pd["date_added"], errors="coerce")

# Add platform
disney_cleaned_pd["platform"] = "Disney+"
netflix_cleaned_pd["platform"] = "Netflix"

# Save cleaned Pandas CSV
disney_cleaned_pd.to_csv("../Data_Resources/disney_pandas_cleaned.csv", index=False)
netflix_cleaned_pd.to_csv("../Data_Resources/netflix_pandas_cleaned.csv", index=False)

print("✅ Pandas-level cleaning complete!")

# =========================================
# STEP 3: START PYSPARK SESSION
# =========================================

spark = SparkSession.builder.appName("MediaCleaning_Pandas_Spark").getOrCreate()

# =========================================
# STEP 4: LOAD CLEANED PANDAS FILES IN SPARK
# =========================================
disney_spark = spark.read.csv("../Data_Resources/disney_pandas_cleaned.csv", header=True, inferSchema=True)
netflix_spark = spark.read.csv("../Data_Resources/netflix_pandas_cleaned.csv", header=True, inferSchema=True)

# =========================================
# STEP 5: CLEANING USING SPARK
# =========================================

# Normalize type column (TV Show → TV)
disney_spark = disney_spark.withColumn("type", regexp_replace(col("type"), "TV Show", "TV"))
netflix_spark = netflix_spark.withColumn("type", regexp_replace(col("type"), "TV Show", "TV"))

# Convert date
disney_spark = disney_spark.withColumn("date_added", to_date(col("date_added")))
netflix_spark = netflix_spark.withColumn("date_added", to_date(col("date_added")))

# Combine datasets
combined_spark = disney_spark.unionByName(netflix_spark)

# Save final PySpark cleaned data
combined_spark.write.mode("overwrite").csv("../Data_Resources/final_cleaned_spark", header=True)

# Summary
print("\n========================")
print("Final Spark Output")
print("========================")
print("Disney rows:", disney_spark.count())
print("Netflix rows:", netflix_spark.count())
print("Combined rows:", combined_spark.count())

combined_spark.show(5, truncate=False)

spark.stop()

