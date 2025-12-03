import sys
import os

from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType

os.environ["JAVA_HOME"]="C:/Program Files/Java/jdk-21"
os.environ["SPARK_HOME"]="C:/RevatureInternshipTraining/week-4-Pyspark/pysparkexamples/.venv/Lib/site-packages/pyspark"
os.environ["PYSPARK_PYTHON"]=sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"]=sys.executable

from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder \
    .appName("Local PySpark") \
    .getOrCreate()

# Get SparkContext
sc = spark.sparkContext


data = [
    (101, "Alice", "HR", 3500),
    (102, "Bob", "IT", 4200),
    (103, "Cathy", "Finance", 3900),
    (104, "David", "IT", 4800),
    (105, "Eva", "HR", 4100)
]
columns = ["EmpID", "Name", "Dept", "Salary"]
emp_df = spark.createDataFrame(data, columns)
emp_df.createOrReplaceTempView("employees")

# 1. Aggregations
agg_df = spark.sql("""
    SELECT Dept,
    COUNT(*) AS Count,
    AVG(Salary) AS Avg_Salary,
    SUM(Salary) AS Total_Salary
    FROM employees
    GROUP BY Dept
    """)
agg_df.show()

# 2. Employees above average
high_earners = spark.sql("""
    SELECT e.Name, e.Dept, e.Salary
    FROM employees e
    JOIN (SELECT Dept, AVG(Salary) AS Avg_Salary
    FROM employees
    GROUP BY Dept) d
    ON e.Dept = d.Dept
    WHERE e.Salary > d.Avg_Salary
    """)
high_earners.show()
# 3. Save results
# high_earners.write.mode("overwrite").parquet("output/high_earners.parquet")

