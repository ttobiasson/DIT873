import matplotlib.pyplot as plotter 
import timeit
import numpy as np


accuracy = "6"
timeList = []

#Vi kanske borde byta axlarna med så att strecken går uppåt, kan vara en god tanke.
# # Men den är ju snabbare fram till att den går över antal kärnor jag har på datorn, 
# Vi får lösa grafen så drar jag över å testar, ok
def generateTime(n):
    for i in range(n):
        workers = str(2**i)
        time = timeit.timeit('m.compute_pi(args)',
                    setup = 'm = __import__("mp-pi-montecarlo-pool");'
                            'import argparse;'
                            'parser = argparse.ArgumentParser(description="Compute Pi using Monte Carlo simulation.");' 
                            'parser.add_argument("-workers", default=' + workers +', type = int);'
                            'parser.add_argument("--accuracy", default=' + accuracy + ', type = int);'
                            'args = parser.parse_args();', 
                    number = 1)
        yield time

gen = generateTime(6)
for i in range(6):
    timeList.append(next(gen))

timeList = np.array(timeList)
#Tror vi får köra ganska hög accuracy för å få grafen fin, aha jaa kanske det. Ajjemän, verkar så. Jag trycker upp den å ser om det går att få något resultat
#gör så
#fick en dunderfin graf nu, jvlar va trevligt!
#tror jag, kolla messenger, men vete fan om man får det konsekvent, det är ju problemet ja, kanske inte blir bättre än såhär, kan vara så
print(timeList)
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