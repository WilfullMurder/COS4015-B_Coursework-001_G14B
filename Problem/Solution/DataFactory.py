import itertools
import string

from CONSTANTS import NUM_OBJECTS, LOCATION_SYNTAX as LS


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

    def convertData(self, i=None):
        tmp = [i[0], i[1], i[2], i[3]]
        self.data.append(tmp.copy())

    def getData(self):
        return self.data

    def getLastIndex(self):
        return len(self.data) - 1

    def getLastElem(self):
        return self.data[len(self.data) - 1]



    def strFromBase(self, num=0, base=0):
        """converts and formats any number to any base <= 169
           :returns converted numString
        """
        if num < 0:
            return '-' + self.strFromBase(self, -num, base)
        (d, m) = divmod(num, base)
        if d > 0:
            return self.strFromBase(self, d, base) + self.digitToChar(m)
        return self.digitToChar(m)

    @staticmethod
    def digitToChar(digit):
        """Converts digit to character from ascii
        :returns chr
        """
        if digit < 10:
            return str(digit)
        return chr(ord('a') + digit - 10)

    @staticmethod
    def addLeadingZeroes(num=""):
        """Formats numStrings in groups of four for readability
            :returns formatted numString
        """
        if len(num) % 4 == 0:
            return num
        while num.__len__() % NUM_OBJECTS > 0:
            num = "0" + num
        return num



