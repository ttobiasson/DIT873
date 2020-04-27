import multiprocessing # See https://docs.python.org/3/library/multiprocessing.html
import argparse # See https://docs.python.org/3/library/argparse.html
import random
from math import pi, fabs


class Arbetarn(multiprocessing.Process):
    def __init__(self, tasks, results):
        multiprocessing.Process.__init__(self)
        self.tasks = tasks
        self.results = results
    def run(self): 
        while True:
            work = self.tasks.get(block = True)
            result = sample_pi(work)
            self.results.put(result)
            self.tasks.task_done()


def sample_pi(n):
    """ Perform n steps of Monte Carlo simulation for estimating Pi/4.
        Returns the number of sucesses."""
    random.seed()
    #print("Hello from a worker")
    s = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1.0:
            s += 1
    return s

def compute_pi(args):
    random.seed(1)
    n = 500
    
    ourPi = pi
    s_total = 0
    n_total = 0
    manager = multiprocessing.Manager()
    tasks = multiprocessing.JoinableQueue()
    results = manager.Queue()
    workers = []
    for _ in range(args.workers):
        worker = Arbetarn(tasks, results)
        workers.append(worker)

    for worker in workers:
        worker.start()
    while True:
        if ourPi > 1/(10**args.accuracy):
            for _ in range(args.workers):
                tasks.put(n)

            tasks.join()
            while not results.empty():
                s_total += results.get()

            n_total += n*args.workers
            pi_est = (4.0*s_total)/n_total
            ourPi = fabs(pi - pi_est)
        else : 
            for worker in workers:
                worker.terminate()
            break

    print(" Steps\tSuccess\tPi est.\tError")
    print("%6d\t%7d\t%1.5f\t%1.5f" % (n_total, s_total, pi_est, pi-pi_est))
    return


