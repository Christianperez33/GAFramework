import random

class Chromosome:
    
    
    def __init__(self, data_dict):
        self.__list__ = [] 
        for options in data_dict:
            self.set(random.choice(options))

            
    def get(self, k):
        return self.__dict__[k]
    
    def set(self, v):
        self.__list__.append(v)
    