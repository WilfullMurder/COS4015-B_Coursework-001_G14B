import itertools
from CONSTANTS import LOCATION_SYNTAX as LS


class DataFactory:
    data = []
    permutations = 0

    def __init__(self):
        self.initData(self)

    def initData(self):
        """ iteration: O(n), sort: O(n log n)"""
        for i in itertools.product(LS, LS, LS, LS):
            if i not in self.data:
                self.convertData(self, i)

        self.data.sort()
        self.permutations = len(self.data)

    def getData(self):
        return self.data

    def getLastIndex(self):
        return len(self.data) - 1

    def convertData(self, i=None):
        tmp= [i[0], i[1], i[2], i[3]]
        self.data.append(tmp.copy())

