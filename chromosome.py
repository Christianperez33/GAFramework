import random
from pprint import pprint
import os

class Chromosome:
    
    def __init__(self, data_dict):
        if isinstance(data_dict, dict):
            self.__dict__ = dict(map(lambda jkey: (jkey,data_dict[jkey]),data_dict))
        else:
            self.__dict__ = {0:data_dict}

                
            
    def get(self, k):
        return self.__dict__[k]
        
    def set(self, k,v):
        self.__dict__[k] = v
        
    def keys(self):
        return self.__dict__.keys()
    
    def values(self):
        return self.__dict__.values()
    