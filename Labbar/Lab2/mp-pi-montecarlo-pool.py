import multiprocessing # See https://docs.python.org/3/library/multiprocessing.html
import argparse # See https://docs.python.org/3/library/argparse.html
import random
from math import pi

def sample_pi(n):
    """ Perform n steps of Monte Carlo simulation for estimating Pi/4.
        Returns the number of sucesses."""
    random.seed()
    print("Hello from a worker")
    s = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1.0:
            s += 1
    return s


def compute_pi(args):
    random.seed(1)
    upperBound = 1.96*(pi/4)*(1-(pi/4))
    n = (int) ((upperBound**2) * (100**args.accuracy))
    
    p = multiprocessing.Pool(args.workers)
    s = p.map(sample_pi, [n]*args.workers)

    n_total = n*args.workers
    s_total = sum(s)
    pi_est = (4.0*s_total)/n_total
    print(" Steps\tSuccess\tPi est.\tError")
    print("%6d\t%7d\t%1.5f\t%1.5f" % (n_total, s_total, pi_est, pi-pi_est))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compute Pi using Monte Carlo simulation.')
    parser.add_argument('--workers', '-w',
                        default='6',
                        type = int,
                        help='Number of parallel processes')
    parser.add_argument('--accuracy', '-d',
                        default='5',
                        type = int,
                        help='Number of digits of accuracy')
    args = parser.parse_args()
    compute_pi(args)
