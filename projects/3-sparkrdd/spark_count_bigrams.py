import sys
from pyspark.sql import SparkSession

def create_bigrams(words):
    return [(words[i], words[i+1]) for i in range(len(words)-1)]

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: spark_count_bigrams.py <file>")
        sys.exit(-1)

    source = sys.argv[1]

    spark = SparkSession.builder.appName("spark-count-bigrams").getOrCreate()
    sc = spark.sparkContext

    lines = sc.textFile(source)

    bigrams = (
        lines
        .map(lambda line: line.lower())
        .map(lambda line: line.split())
        .flatMap(create_bigrams)
    )

    counts = (
        bigrams
        .map(lambda pair: (pair, 1))
        .reduceByKey(lambda a, b: a + b)
    )

    results = counts.collect()

    print("\n" + "-"*40)
    for (w1, w2), total in results:
        print(f"{w1} {w2} -> {total}")
    print("-"*40 + "\n")

    spark.stop()