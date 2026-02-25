import sys
from pyspark.sql import SparkSession

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: spark_count_people.py <file>")
        sys.exit(-1)

    source = sys.argv[1]

    spark = SparkSession.builder.appName("spark-count-people").getOrCreate()
    sc = spark.sparkContext

    lines = sc.textFile(source)

    city_pairs = (
        lines
        .map(lambda line: line.split())
        .map(lambda parts: (parts[2], 1))
    )

    counts = city_pairs.reduceByKey(lambda a, b: a + b)

    results = counts.collect()

    print("\n" + "-"*40)
    for city, total in results:
        print(city, total)
    print("-"*40 + "\n")

    spark.stop()