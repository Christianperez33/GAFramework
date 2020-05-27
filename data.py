import numpy as np
import json
import os
from os.path import isfile, join
from os import listdir


class Data:

    def __init__(self, path):
        self.path = path if not os.path.isdir(path) else " "
        self.dirPath = path if os.path.isdir(path) else " "
        # first row = x jobs and y machines, 1 machine per operation
        # second row: job 1 has 6 operations, the first operation can be processed by 1 machine that is machine 3 with processing time 1.
        self.json = self.load() if not os.path.isdir(path) else self.loadDirectory()

    def load(self):
        input = open(self.path, 'r').readlines()
        res = {"config": {}, "data": {}}
        for i in range(len(input)):
            row = list(filter(('').__ne__, input[i].split(" ")[:-2]))
            if i == 0:
                res["config"] = dict(
                    zip(["njobs", "nmachines", "machine/operation"], row))
            else:
                res["data"][str(i)] = {}
                res["data"][str(i)]["operation/job"] = row[0]
                res["data"][str(i)]["machine/time"] = []
                mtime = 1
                while mtime <= len(row[1:]):
                    tuples = row[mtime+1:  1+mtime+(int(row[mtime]) * 2)]
                    res["data"][str(i)]["machine/time"].append(list(zip(tuples[::2], tuples[1::2])))
                    mtime += 1 + (int(row[mtime]) * 2)

        return res

    def loadDirectory(self):
        res = {}
        for p in [f for f in listdir(self.dirPath)]:
            self.path = join(self.dirPath, p)
            res[p] = self.load()
            
        return res
    
