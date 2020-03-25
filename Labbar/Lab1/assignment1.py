import matplotlib.pyplot as plotter 
import montecarlo
import timeit
import argparse
#'time', '/home/tom/DIT873/Labbar/Lab1/montecarlo.py', '-w', '1', '-s', '1000000'
parser = argparse.ArgumentParser(description='Compute Pi using Monte Carlo simulation.')
parser.add_argument('--workers', '-w',
                        default='1',
                        type = int,
                        help='Number of parallel processes')
parser.add_argument('--steps', '-s',
                        default='1000',
                        type = int,
                        help='Number of steps in the Monte Carlo simulation')
args = parser.parse_args()
tidendettog = timeit.timeit(str(montecarlo.compute_pi(args)))
print(tidendettog)

y1 = [1, 2, 4, 8, 16, 32]
x1 = [1/x for x in y1]

plotter.plot(x1, y1, label = "theoretical") 
  #
x2 = [12,42,3] 
y2 = [4,1,3] 
plotter.plot(x2, y2, label = "measured") 
  
plotter.xlabel('Time in S') 
plotter.ylabel('Number of cores') 
plotter.title('Parallelization graph') 
  
plotter.legend() 
plotter.show() 