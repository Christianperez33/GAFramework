import random

class Chromosome:
    
    def __init__(self, data_dict):
        self.__list__ = [] 
        for options in data_dict:
            self.set(random.choice(options))
            
    def get(self, k):
        return self.__dict__[k]
    
    def set(self, v):
        self.__list__.append((v[0],int(v[1])))
    
    def keys(self):
        return [x for x,y in self.__list__]
    
    def values(self):
        return [y for x,y in self.__list__]
    