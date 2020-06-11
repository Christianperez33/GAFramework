from chromosome import Chromosome
import os


class Population:

    def __init__(self, data_dict):
        for k in data_dict['data']:
            data = data_dict['data'][k]
            self.__dict__[k] = Chromosome(data["machine/time"])

    def get(self, k):
        return self.__dict__[k]

    def set(self, k, v):
        self.__dict__[k] = v

    def keys(self):
        return list(self.__dict__.keys())

    def values(self):
        return list(self.__dict__.values())
