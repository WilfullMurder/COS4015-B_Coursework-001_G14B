import itertools


class DataFactory:
    data = []

    def __init__(self):
        for i in itertools.product([0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]):
            if i not in self.data:
                self.data.append(i)

        self.data.sort()


