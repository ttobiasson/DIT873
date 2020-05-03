from pyspark import SparkContext
import numpy as np
def goodFunction():
    sc = SparkContext(master = 'local[4]')

    distFile = sc.textFile("/home/tom/Downloads/assignment3.dat")

    list = distFile.map(lambda l: l.split('\t')) \
                   .map(lambda t: float(t[2]))
    
    
    list2 = list.take(100000000)
    
    sd = list.stdev()
    mean = list.mean()
    mini = list.min()
    maxi = list.max()
    histogram, edges = np.histogram(list2, range=(mini, maxi))

    print("Standard Deviation: " + str(sd))
    print("Mean: " + str(mean))
    print("Minimum Value: " + str(mini))
    print("Maximum Value: " + str(maxi))
    print("Histogram Edges: " + str(edges))
    print("Histogram Values: " + str(histogram))


if __name__ == "__main__":
    goodFunction()