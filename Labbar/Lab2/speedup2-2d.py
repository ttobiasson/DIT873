import matplotlib.pyplot as plotter 
import timeit
import numpy as np


timeList = []
#konstigt att det ska vara så olika hela tiden hurbra det ska va
k_clusters = 1
iterations = str(100)
samples = str(50000)
def generateTime(n):
    for i in range(n):
        workers = str(2**i)
        time = timeit.timeit('m.computeClustering(args)',
                    setup = 'm = __import__("problem2-2d");'
                            'import argparse;'
                            'parser = argparse.ArgumentParser("description=Compute a k-means clustering.", epilog = "Example: kmeans.py -v -k 4 --samples 10000 --classes 4 --plot result.png");'
                            'parser.add_argument("-workers", default=' + workers +', type = int);'
                            'parser.add_argument("--k_clusters", "-k",default="3",type = int,help="Number of clusters");'
                            'parser.add_argument("--iterations", "-i",default='+iterations+',type = int,help="Number of iterations in k-means");'
                            'parser.add_argument("--samples", "-s", default='+samples+',type = int,help="Number of samples to generate as input");'
                            'parser.add_argument("--classes", "-c",default="3",type = int,help="Number of classes to generate samples from");' 
                            'parser.add_argument("--plot", "-p",default="abel.png", type = str,help="Filename to plot the final result");'   
                            'parser.add_argument("--verbose", "-v",action="store_true",help="Print verbose diagnostic output");'
                            'parser.add_argument("--debug", "-d",action="store_true",help="Print debugging output");'
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
plotter.ylabel('Speedup') 
plotter.title('Parallelization graph') 
  
plotter.legend() 
plotter.show()
#plotter.savefig('graf.png')
