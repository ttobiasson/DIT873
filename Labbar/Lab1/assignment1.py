import matplotlib.pyplot as plotter 
import montecarlo
import timeit


workers = "1"
steps = "100000000"

def generateTime(n):
    for i in range(n):
        workers = str(2**i)
        print(i)
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
timeList = []
for i in range(6):
    timeList.append(next(gen))

y1 = [1, 2, 4, 8, 16, 32]
x1 = [x for x in timeList]

plotter.plot(x1, y1, label = "theoretical") 

x2 = [12,42,3] 
y2 = [4,1,3] 
plotter.plot(x2, y2, label = "measured") 
  
plotter.xlabel('Time in S') 
plotter.ylabel('Number of cores') 
plotter.title('Parallelization graph') 
  
plotter.legend() 
plotter.show() 