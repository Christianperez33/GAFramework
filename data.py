import os
from os import listdir
from os.path import isfile, join
import numpy as np


class Data:
    def __init__(self,path):
        # Base data
        # ['J', '#machId jobPred jobSucc setupTime']
        # J = procTime energyConsddate weight rdate
        self.__dict__ = {}
        self.path = path
        self.onlyfiles = [join(self.path, f) for f in listdir(self.path)]
        self.__dict__ = self.getAllData()
        
        
        
    def getAllData(self):
        sol = {}
        for file in self.onlyfiles:
            key = file.split("/")[-1].split(".")[0]
            sol[key] = {}
            with open(file,"r") as f:
                for row  in f.read().splitlines():
                    if row == '':
                        continue
                    elif '#' in row:
                        if "#num jobs" == row:
                            sol[key]["J"] = []
                        elif "#jobId ddate weight rdate" == row:
                            sol[key]["J_data"] = sol[key]["J"].copy()
                        elif "#machId jobPred jobSucc setupTime" == row:
                            sol[key]["Mps"] = {}
                        else:
                            sol[key][row] = []
                    else:
                        if list(sol[key].keys())[-1] == "J":
                            sol[key][list(sol[key].keys())[-1]] = dict(zip(range(1,int(row)+1),np.repeat([],len(range(1,int(row)+1))) ))
                            
                        elif list(sol[key].keys())[-1] == "#jobId machId procTime energyCons":
                            row_data = (row.replace('\t',' ')).split(' ')
                            if int(row_data[0]) not in sol[key]["J"].keys():
                                sol[key]["J"][int(row_data[0])] = {}
                            
                            sol[key]["J"][int(row_data[0])][int(row_data[1])]=list(map(lambda x : float(x.replace(",",".")), row_data[2:]))
                            
                        elif list(sol[key].keys())[-1] == "J_data" :
                            row_data = (row.replace('\t',' ')).split(' ')
                            sol[key]["J_data"][int(row_data[0])] = row_data[1:]
                        
                        elif list(sol[key].keys())[-1] == "Mps" :
                            row_data = (row.replace('\t',' ')).split(' ')
                            if int(row_data[0]) not in sol[key]["Mps"].keys():
                                sol[key]["Mps"][int(row_data[0])] = []
                            sol[key]["Mps"][int(row_data[0])].append(row_data[1:])
                        else:
                            sol[key][list(sol[key].keys())[-1]] = sol[key][list(sol[key].keys())[-1]]+[(row.replace('\t',' ')).split(' ')]
            f.close()
            del sol[key]["#jobId machId procTime energyCons"]
            sol[key]["#num jobs"] = len(sol[key]["J"])
            sol[key]["#num machines"] = int(sol[key]["#num machines"][0][0])
        return sol
    


    