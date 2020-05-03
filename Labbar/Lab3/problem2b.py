from pyspark import SparkContext
import numpy as np
def goodFunction():
    sc = SparkContext(master = 'local[8]')

    distFile = sc.textFile("/home/botvinnik/DIT873/Labbar/Lab3/assignment3.dat")

    list = distFile.map(lambda l: l.split('\t')) \
                   .map(lambda t: float(t[2]))
    
    
    sd = list.stdev()
    mean = list.mean()
    mini = list.min()
    maxi = list.max()
    median = np.median(list.collect())
    histogram, bins = list.histogram(10)

    print("Standard Deviation: " + str(sd))
    print("Mean: " + str(mean))
    print("Minimum Value: " + str(mini))
    print("Maximum Value: " + str(maxi))
    print("Histogram Bins: " + str(bins))
    print("Histogram: " + str(histogram))
    print("Median: " + str(median))



if __name__ == "__main__":
    goodFunction()