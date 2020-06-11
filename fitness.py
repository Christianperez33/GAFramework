import numpy as np

def getMakespanJob(chromosome):
    return np.sum(chromosome.values())

def getMakespanPoulation(population):
    return np.sum(list(map(lambda x: getMakespanJob(population.__dict__[x]) , population.__dict__)))

# get makespan from population object
def getMakespan(population):
    return list(map(lambda x: np.sum(list(map(lambda y: getMakespanJob(y),population[x].values()))), population))
    