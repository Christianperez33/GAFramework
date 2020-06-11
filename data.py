import os
from os import listdir
from os.path import isfile, join
import numpy as np


class Data:
    def __init__(self,path):
        self.path = path
        self.onlyfiles = [join(self.path, f) for f in listdir(self.path)]
        # Base data
        # ['#num jobs', '#num machines', '#jobId machId procTime energyCons', '#jobId ddate weight rdate', '#machId jobPred jobSucc setupTime']
        self.__dict__ = self.getAllData()
        
        # #  [jobId machId procTime energyCons ddate weight rdate]
        # self.jobData = self.getTimeData()
        # self.processingTime = self.processingTime()
        # self.earlyStart = self.earlyStart()
        
        
    def getAllData(self):
        sol = {}
        for file in self.onlyfiles:
            key = file.split("/")[-1].split(".")[0]
            sol[key] = {}
            with open(file,"r") as f:
                for row  in f.read().splitlines():
                    if row == '':
                        continue
                    if '#' in row:
                        
                        if "#num jobs" == row:
                            sol[key]["J"] = []
                        elif "#jobId ddate weight rdate" == row:
                            sol[key]["J_data"] = sol[key]["J"]
                        else:
                            pass
                            sol[key][row] = []
                    else:
                        if list(sol[key].keys())[-1] == "J":
                            sol[key][list(sol[key].keys())[-1]] = dict(zip(range(1,int(row)+1),np.repeat({},len(range(1,int(row)+1))) ))
                        elif list(sol[key].keys())[-1] == "#jobId machId procTime energyCons":
                            row_data = (row.replace('\t',' ')).split(' ')
                            sol[key]["J"][int(row_data[0])][int(row_data[1])] = row_data[2:]
                        elif list(sol[key].keys())[-1] == "J_data" :
                            row_data = (row.replace('\t',' ')).split(' ')
                            sol[key][list(sol[key].keys())[-1]][int(row_data[0])] = row_data[1:]
                        else:
                            sol[key][list(sol[key].keys())[-1]] = sol[key][list(sol[key].keys())[-1]]+[(row.replace('\t',' ')).split(' ')]
                
                f.close()
            del sol[key]["#num machines"]
            del sol[key]["#jobId machId procTime energyCons"]
            print(sol[key].keys())
        return sol
    
    # def getTimeData(self):
    #     sol = {}
    #     for d in self.data:
    #         sol[d] = []
    #         jdata = self.data[d]['#jobId machId procTime energyCons']
    #         extra = {x[0] : x[1:] for x in self.data[d]['#jobId ddate weight rdate']}
    #         for j in jdata:
    #              sol[d] = sol[d] + [j+extra[j[0]]]
    #     return sol
    
    # def processingTime(self):
    #     T = {}
    #     for x in self.jobData:
    #         T[x] = {}
    #         data = self.jobData[x]
    #         for d in data:
    #             valor = float(d[2].replace(",","."))
    #             if d[0] not in T[x].keys():
    #                 T[x][d[0]] = valor
    #             else:
    #                 T[x][d[0]] = int(T[x][d[0]]) + valor
            
                
    #         T[x] = {k: [v/ i for i in T[x].values()] for k, v in T[x].items()}
    #     return T
    
    # def earlyStart(self):
    #     E = {}
    #     for x in self.jobData:
    #         E[x] = {}
    #         data = self.jobData[x]
    #         for d in data:
    #             valor = float(d[2].replace(",","."))
    #             if d[0] not in E[x].keys():
    #                 E[x][d[0]] = valor
    #             else:
    #                 E[x][d[0]] = int(E[x][d[0]]) + valor
    #     return E
    
    # def getMachineJobTime(self):
    #     sol = {}
    #     for k in self.data:
    #         sol[k] = {}
    #         for d in  self.data[k]['#machId jobPred jobSucc setupTime']:
    #             if d[0] not in sol[k].keys():
    #                 sol[k][d[0]] = {}
    #             if d[2] not in sol[k][d[0]].keys():
    #                 sol[k][d[0]][d[2]] = float(d[3].replace(",","."))
    #             else:
    #                 sol[k][d[0]][d[2]] = sol[k][d[0]][d[2]]+ float(d[3].replace(",","."))

    #     for k in sol:
    #         datos = sol[k]
    #         res = {}
    #         for d in datos:
    #             res.update(datos[d])
    #         sol[k] = res
    
    #     return sol


    