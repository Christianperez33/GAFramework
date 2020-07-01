from chromosome import Chromosome
from phenotype import Phenotype
import os



class Population:

    def __init__(self, data_dict, nphenom):
        self.__dict__ = dict(map(lambda x: (x,Chromosome(data_dict[x]))   , data_dict ))
        self.__phenotype__ = list(map(lambda x : Phenotype(data_dict["J"]) ,list(range(nphenom))))

    def get(self, k):
        return self.__dict__[k]

    def set(self, k, v):
        self.__dict__[k] = v

    def getPhenotype(self, k):
        return self.__phenotype__[k]

    def addPhenotype(self, v):
        if  isinstance(v,list):
            self.__phenotype__ += v
        else:
            self.__phenotype__.append(v)
    
    def keys(self):
        return list(self.__dict__.keys())

    def values(self):
        return list(self.__dict__.values())
