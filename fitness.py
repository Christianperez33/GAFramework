import numpy as np
import math
class Fitness:
    
    def __init__(self,population):
        self.population = population
        self.makespan = []
        self.energyCons = []
        self.get()
        
    def get(self):
        for phenotype in self.population.__phenotype__ :
            self.makespan.append(np.sum(list(map(lambda x : x[1][1],phenotype.__dict__.items()))))
            self.energyCons.append(np.sum(list(map(lambda x : x[1][2],phenotype.__dict__.items()))))