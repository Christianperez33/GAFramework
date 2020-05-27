
class Fitness:
       
    def get(self, k):
        return self.__dict__[k]
    
    def set(self, k, v):
        self.__dict__[k] = v