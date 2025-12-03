from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName('Local PySpark') \
    .getOrCreate()


sc=spark.sparkContext

numbers=[1,2,3,4,5]
rdd=sc.parallelize(numbers)
print("Original RDD:", rdd.collect())

doubled=rddnum.map(lambda x:x*2)
print('type: ',type(doubled))
print("Doubled: ",doubled.collect())

evennum=rddnum.filter(lambda x:x%2==0)
print('type: ',type(evennum))
print("Even Numbers: ", evennum.collect())

total=rddnum.reduce(lambda a,ab: a+b)
print('type: ',type(total))
print("Sum: ",total)

lines=sc.parallelize(["hello world", "hello spark", "hello RDD"])
words=lines.flatMap(lambda line: line.split(" "))
print(words.collect())
words=lines.words.map(lambda word:(word,1))
print(word_pairs.collect())
word_counts=lines.word_pairs.reduceByKey(lambda a,b: a+b)
print("Word Count:",word_counts.collect())

data= [("Alice", 25),("Bob", 30),("Charlie",28)]
df= spark.createDataFrame(data,["Name", "Age"])
df.show()
