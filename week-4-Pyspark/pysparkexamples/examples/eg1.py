import sys
import os

os.environ["JAVA_HOME"]="C:/Program Files/Java/jdk-21"
os.environ["SPARK_HOME"]="C:/RevatureInternshipTraining/week-4-Pyspark/pysparkexamples/.venv/Lib/site-packages/pyspark"
os.environ["PYSPARK_PYTHON"]=sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"]=sys.executable


from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName('Local PySpark') \
    .getOrCreate()

from pyspark.sql.types import StructType, StructField, StringType, IntegerType

schema = StructType([
    StructField('Name', StringType(), True),
    StructField('Age', IntegerType(), True),
])

data=[("Alice", 25),("Bob", 30)]
df=spark.createDataFrame(data, schema)
print('Schema')
df.printSchema()
print('DataFrame')
df.show()


