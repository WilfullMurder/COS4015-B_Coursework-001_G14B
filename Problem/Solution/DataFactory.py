import itertools
from CONSTANTS import LOCATION_SYNTAX as LS


class DataFactory:
    data = []

    def __init__(self):
        for i in itertools.product(LS, LS, LS, LS):
            if i not in self.data:
                self.data.append(i)

        self.data.sort()
