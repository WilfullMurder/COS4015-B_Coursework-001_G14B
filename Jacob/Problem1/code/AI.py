from State import State
import matplotlib.pyplot as plt
import numpy as np
from sklearn import tree




class AI:
    startState = []
    endState = []

    numStates = 3
    numObjects = 4
    permutations = int(pow(numStates, numObjects))

    def AI(self):
        self.init()

    def init(self):
        self.startState = State.State(0, 0, 0, 0)
        self.endState = State.State(2, 2, 2, 2)

    def run(self):
        graph = None

    def generateDecisionTree(self):
        pass

    def getSolution(self, graph=None):
        pass

    def displayGraph(self, graph=None):
        pass

    def addLeadingZeros(self, number=""):
        pass
