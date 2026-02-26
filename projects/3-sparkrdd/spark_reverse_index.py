import sys
import json
import re
from pyspark.sql import SparkSession

WORD_RE = re.compile(r"[a-zA-Z]+")

def parse_article(line):
    try:
        obj = json.loads(line)
        docid = obj["identifier"]
        text = obj.get("abstract", "")
        words = set(w.lower() for w in WORD_RE.findall(text))
        return [(word, docid) for word in words]
    except:
        return []
def parse_article(line):
    try:
        obj = json.loads(line)   
        docid = obj.get("identifier")
        article_body = obj.get("article_body", {})
        text = article_body.get("wikitext", "")
        if not docid or not text:
            return []
        words = set(w.lower() for w in WORD_RE.findall(text))
        return [(word, docid) for word in words]
    except Exception:
        return []
if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: spark_reverse_index.py <input> <output>")
        sys.exit(-1)

    source = sys.argv[1]
    output = sys.argv[2]

    spark = SparkSession.builder.appName("spark-reverse-index").getOrCreate()
    sc = spark.sparkContext

    lines = sc.textFile(source)

    word_doc_pairs = lines.flatMap(parse_article)

    index = word_doc_pairs.aggregateByKey(
        set(),
        lambda acc, v: acc | {v},
        lambda acc1, acc2: acc1 | acc2
    )

    formatted = index.map(lambda x: x[0] + " " + " ".join(sorted(str(doc) for doc in x[1])))

    formatted.saveAsTextFile(output)

    spark.stop()