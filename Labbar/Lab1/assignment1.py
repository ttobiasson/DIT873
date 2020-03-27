import matplotlib.pyplot as plotter 
import timeit


steps = "10000000"

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

x1 = [1, 2, 4, 8, 16, 32]
y1 = [1/((1-(0.95))+((0.95)/x)) for x in x1]

plotter.plot(x1, y1, label = "theoretical") 

x2 = [1, 2, 4, 8, 16, 32]
y2 = [y for y in timeList] 
plotter.plot(x2, y2, label = "measured") 
  
plotter.xlabel('Number of cores') 
plotter.ylabel('Time in S') 
plotter.title('Parallelization graph') 
  
plotter.legend() 
plotter.show() 