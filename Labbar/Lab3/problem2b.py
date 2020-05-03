from pyspark import SparkContext
import numpy as np
import argparse

def goodFunction(args):
    sc = SparkContext(master = 'local[' + args.cores + ']')

    distFile = sc.textFile(args.file)

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
    parser = argparse.ArgumentParser()

    parser.add_argument('--cores', '-c',
                        default='1',
                        type = str,
                        help='Number of cores')
    parser.add_argument('--file', '-f',
                        type=str,
                        help='File to use')

    args = parser.parse_args()

    goodFunction(args)