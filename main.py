from GA import GA
from data import Data
import time
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument('-i', '--iter', help='Iteraciones que realiza el algoritmo', default=50, type=int)
argparser.add_argument('-is', '--initsol', help='Tamaño inicial de la población', default=50, type=int)
args = argparser.parse_args()

start_time = time.time()
ga = GA(args.iter,args.initsol)
ga.__start__()
ga.__results__()
print("--- %s seconds ---" % str(time.time() - start_time))



