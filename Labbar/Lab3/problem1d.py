from mrjob.job import MRJob
import re
import numpy as np

class MRGoodJob(MRJob):

    def mapper_init(self):
        self.group = self.options.group

    def configure_args(self):
        super(MRGoodJob, self).configure_args()
        self.add_passthru_arg('--group',default = 12, type=int)

    def mapper(self, _, line):
        list = re.split(r'\t', line)
        if int(list[1]) == self.group:
            yield 1, float(list[2])

    def reducer(self, key, numbers):
        ns = [number for number in numbers]
        
        minimum = min(ns)
        maximum = max(ns)
        sd = np.std(ns)
        mean = np.mean(ns)
        histogram, bins = np.histogram(ns)
        
        yield "Standard Deviation", sd
        yield "Mean", mean
        yield "Minimum", minimum
        yield "Maximum", maximum
        yield "Bins", bins.tolist()
        yield "Histogram", histogram.tolist()

if __name__ == '__main__':
    MRGoodJob.run()
