import matplotlib.pyplot as plotter 
import timeit
import numpy as np


steps = "10000000"
timeList = []


def generateTime(n):
    for i in range(n):
        workers = str(2**i)
        time = timeit.timeit('montecarlo.compute_pi(args)',
                    setup = 'import montecarlo;' 
                            'import argparse;'
                            'parser = argparse.ArgumentParser(description="Compute Pi using Monte Carlo simulation.");' 
                            'parser = argparse.ArgumentParser(description="Compute Pi using Monte Carlo simulation.");'
                            'parser.add_argument("-workers", default=' + workers +', type = int);'
                            'parser.add_argument("--steps", default=' + steps + ', type = int);'
                            'args = parser.parse_args();', 
                    number = 1)
        yield time

gen = generateTime(6)
for i in range(6):
    timeList.append(next(gen))

timeList = np.array(timeList)

x2 = [1, 2, 4, 8, 16, 32]
y2 = timeList
plotter.plot(x2, y2[0]/y2, label = "measured") 

x1 = [1, 2, 4, 8, 16, 32]
y1 = x1

plotter.plot(x1, y1, label = "theoretical") 
  
plotter.xlabel('Number of cores') 
plotter.ylabel('Time in S') 
plotter.title('Parallelization graph') 
  
plotter.legend() 
plotter.show()
#plotter.savefig('graf.png')