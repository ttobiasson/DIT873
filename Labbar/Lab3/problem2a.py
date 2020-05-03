import pyspark
import numpy as np
sc = pyspark.SparkContext(master = 'local[4]')

distFile = sc.textFile("/home/tom/Downloads/assignment3.dat")

sd = distFile.map(lambda l: l.split(r'\t'))  \
            .map(lambda l: float(l[2]), 1) \
            .reduceByKey(lambda x, y: x+y)
cc = sd.collect()
print(cc)