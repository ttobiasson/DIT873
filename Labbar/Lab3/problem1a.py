from mrjob.job import MRJob
import re
import numpy as np

NUMBERS_RE = re.compile(r'[1-9]+\.[0-9]+$')

class MRGoodJob(MRJob):

    def mapper(self, _, line):
        for number in NUMBERS_RE.findall(line):
            yield 1, float(number)

    def reducer(self, key, numbers):
        ns = [number for number in numbers]
        
        minimum = min(ns)
        maximum = max(ns)
        sd = np.std(ns)
        mean = np.mean(ns)
        histogram, edges = np.histogram(ns)
        yield "Standard Deviation", sd
        yield "Mean", mean
        yield "Minimum", minimum
        yield "Maximum", maximum
        yield "Edges", edges.tolist()
        yield "Histogram", histogram.tolist()

if __name__ == '__main__':
    MRGoodJob.run()
