import random
import os
from pprint import pprint

class Phenotype:
    
    def __init__(self, data_dict):
        if isinstance(data_dict[list(data_dict.keys())[0]],list):
            self.__dict__ = data_dict
        else:
            self.__dict__ = dict(map(lambda jkey: (jkey,list(data_dict[jkey].items())[random.choice(list(range(len(data_dict[jkey].items()))))]) ,data_dict))
            self.__dict__ = dict([(key,[self.__dict__[key][0]]+self.__dict__[key][1]) for key in self.__dict__])
            
    def get(self, k):
        return self.__dict__[k]
        
    def set(self,k, v):
        self.__dict__[k] = v
        
    