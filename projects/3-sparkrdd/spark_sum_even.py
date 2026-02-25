import sys
from pyspark.sql import SparkSession

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: spark_sum_even.py <file>")
        sys.exit(-1)

    source = sys.argv[1]

    spark = SparkSession.builder.appName("spark-sum-even").getOrCreate()
    sc = spark.sparkContext

    lines = sc.textFile(source)

    numbers = (
        lines
        .flatMap(lambda line: line.split())
        .map(lambda x: int(x))
    )

    even_numbers = numbers.filter(lambda x: x % 2 == 0)

    total = even_numbers.sum()

    print("\n" + "-"*40)
    print("SUM OF EVEN NUMBERS =", total)
    print("-"*40 + "\n")

    spark.stop()