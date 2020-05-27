from data import Data
from population import Population
from os import listdir

data = Data("./data/Dauzere_Data/")
problems = {}
for file in data.json:
    problems[file] = Population(data.json[file])


