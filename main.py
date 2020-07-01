from GA import GA
from data import Data
import time
start_time = time.time()


ga = GA(1)
ga.__start__()
ga.__results__()
print("--- %s seconds ---" % str(time.time() - start_time))



