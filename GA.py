
import os
import copy
import random
from pprint import pprint
import numpy as np
from os import listdir
from data import Data
from fitness import Fitness
from phenotype import Phenotype
from population import Population
from tqdm import tqdm


class GA:
     
    def __init__(self,iter = 50,ninitsol = 50, mutation = 0.05, crossover = 0.5):
        self.iter = iter
        self.mutation = mutation
        self.crossover = crossover
        self.ninitsol = ninitsol
        self.data = Data("./data/Source_30_4")
        self.population = self.initPopulation()
        
    
    def initPopulation(self):
        res = {}
        for file in self.data.__dict__:
            res[file] = Population(self.data.__dict__[file],self.ninitsol)
        return res

    def __start__(self):
        for i in tqdm(range(self.iter)):
            for p in self.population:
                fitness = Fitness(self.population[p])
                selection = self.__selection__(self.population[p])
                crossover = self.__crossover__(selection)
                self.population[p].addPhenotype(crossover)
                mutation = self.__mutation___(self.population[p])      
    
    def __selection__(self, population):
        index = np.arange(population.__dict__["#num jobs"].__dict__[0])
        np.random.shuffle(index)
        couple_index = list(zip(index[::2],index[1:][::2]))
        return list(map( lambda x: [population.__phenotype__[x[0]],population.__phenotype__[x[1]]]  ,couple_index ))
    
    def __crossover__(self, population):
        aux = []
        for f,m in population:
            index = np.arange(int(len(f.__dict__)))
            np.random.shuffle(index)
            son1 = dict(np.concatenate((np.array(list(f.__dict__.items()))[index[:int(len(f.__dict__)*self.crossover)]],np.array(list(m.__dict__.items()))[index[int(len(f.__dict__)*self.crossover):]]) ))
            son1 = Phenotype(son1)
            son2 = dict(np.concatenate((np.array(list(f.__dict__.items()))[index[int(len(f.__dict__)*self.crossover):]],np.array(list(m.__dict__.items()))[index[:int(len(f.__dict__)*self.crossover)]]) ))
            son2 = Phenotype(son2)
            aux += [son1,son2]
        return aux

    def __mutation___ (self,population):
        for indx in random.sample(list(np.arange(len(population.__phenotype__)+1)),int(len(population.__phenotype__)*self.mutation)):
            phe = copy.deepcopy(population.__phenotype__[indx-1])
            indx_phe = random.sample(list(phe.__dict__),int(len(phe.__dict__)*self.mutation))
            for ip in indx_phe:
                data = copy.deepcopy(population.__dict__['J'].__dict__[ip])
                aux = [int(phe.__dict__[ip][0]),data[int(phe.__dict__[ip][0])]]
                del data[int(phe.__dict__[ip][0])]
                subs = list(random.choice(list(data.items()))) if data else aux
                subs[1].insert(0,subs[0])
                phe.__dict__[ip] = subs[1]
        return population
    
    def __results__(self):
        fitness = dict(map(lambda x: (x,Fitness(self.population[x])) ,self.population))
        fitness = dict(map(lambda x: (x,{"makespan":[max(fitness[x].makespan),min(fitness[x].makespan)],"energycons":[max(fitness[x].energyCons),min(fitness[x].energyCons)]}) ,fitness))
        pprint(fitness)
        
        
        
            
    
                
                
        
    


