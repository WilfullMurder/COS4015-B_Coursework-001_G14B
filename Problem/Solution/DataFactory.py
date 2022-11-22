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

    def digitToChar(self,digit):
        if digit < 10:
            return str(digit)
        return chr(ord('a') + digit - 10)

    def strFromBase(self, num=0, base=0):
        if num<0:
            return '-' + self.strFromBase(self, -num, base)
        (d,m) = divmod(num, base)
        if d > 0:
            return self.strFromBase(self, d, base) + self.digitToChar(self, m)
        return self.digitToChar(self, m)

    def addLeadingZeroes(self, num=""):
        if num.isnumeric():
            while num.__len__() < 4:
                num = "0" + num
            return num
