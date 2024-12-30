# -*- coding: utf-8 -*-
"""exe_spark.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/152AsGHIVT0Dq85O4dVmIrL7tUmuG5HXQ
"""

!pip install pyspark

from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").appName("WordCount").getOrCreate()
print("SparkSession foi criado")

https://raw.githubusercontent.com/AndreBomfim99/PB-ANDRE-BOMFIM-DA-SILVA/refs/heads/main/README.MD?token=GHSAT0AAAAAAC3LHA4RJBMXHILMPTQREHKCZ3EE7MA -O README.md

!ls -l README.md

rdd = spark.sparkContext.textFile("README.md")

words = rdd.flatMap(lambda line: line.split())
word_counts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)


for word, count in word_counts.collect():
    print(f"{word}: {count}")

output_file = "palavras_contadas.txt"

with open(output_file, "w") as f:
    for word, count in word_counts.collect():
        f.write(f"{word}: {count}\n")

from google.colab import files
files.download(output_file)

import csv
from google.colab import files

output_csv = "quantidade_palavras.csv"

with open(output_csv, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Palavra", "N. ocorrências"])
    for word, count in word_counts.collect():
        writer.writerow([word, count])

files.download(output_csv)