from data import Data
from population import Population
from os import listdir
import numpy as np
import fitness as Fitness

import random

class GA:
     
    def __init__(self,iter = 50, mutation = 0.05, crossover = 0.5):
        self.data = Data("./data/Source_30_4")
        self.population = self.initPopulation()
        self.iter = iter
        self.mutation = mutation
        self.crossover = crossover
    
    def initPopulation(self):
        res = {}
        for file in self.data.json:
            res[file] = Population(self.data.json[file])
        return res
    
    def __selection__(self, population):
        index = np.arange(len(population.__dict__))
        np.random.shuffle(index)
        twice_index = list(zip(index[::2],index[1:][::2]))
        
        return list(map( lambda x: [population.values()[x[0]],population.values()[x[1]]]  ,twice_index ))
    
    def __crossover__(self, population):
        for f,m in population:
            print(random.sample(f.__list__, int(len(f.__list__)*self.crossover)))
            
    def __start__(self):
        for i in range(self.iter):
            for p in self.population:
                valor_fitness = Fitness.getMakespanPoulation(self.population[p])
                selection = self.__selection__(self.population[p])
                crossover = self.__crossover__(selection)
                
                
        
    


