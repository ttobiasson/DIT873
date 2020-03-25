import matplotlib.pyplot as plotter 
import montecarlo

x1 = [1, 2, 4, 8, 16, 32] 
y1 = [x for x in x1] 
plotter.plot(x1, y1, label = "theoretical") 
  #
x2 = [12,42,3] 
y2 = [4,1,3] 
plotter.plot(x2, y2, label = "measured") 
  
plotter.xlabel('Time in S') 
plotter.ylabel('Number of cores') 
plotter.title('Parallelization graph') 
  
# show a legend on the plot 
plotter.legend() 
  
# function to show the plot 
plotter.show() 