import pandas as pd
from sklearn.preprocessing import OneHotEncoder

import BST
import State
from CONSTANTS import *
from DataFactory import DataFactory
from Graph import Graph
from State import State as St
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn import tree, svm


class AI:
    startState = None
    endState = None
    poss_States = []
    bst = None
    permutations = 0

    def AI(self):
        self.init(self)

    def init(self):
        self.startState = St
        self.endState = St
        self.startState.State(self.startState, 0, 0, 0, 0)
        self.endState.State(self.endState, 2, 2, 2, 2)
        self.permutations = int(pow(NUM_STATES, NUM_OBJECTS))
        self.bst = BST.BinarySearchTree

    def run(self):
        self.bst.__init__(self.bst, self.startState.toString(self.startState))
        currentState = []
        vaildStates = 0
        currentState = St
        for i in range(self.permutations):
            for k in range(NUM_OBJECTS):

                currentState.State(currentState, k % NUM_STATES, k % NUM_STATES, k % NUM_STATES, k % NUM_STATES)
                if currentState not in self.poss_States:
                    self.poss_States.append(currentState.state.copy())
                for j in range(NUM_STATES):
                    currentState.State(currentState, j, k % NUM_STATES, j, k % NUM_STATES)
                    if currentState not in self.poss_States:
                        self.poss_States.append(currentState.state.copy())

                    print(currentState.toString(currentState))

            if currentState.isValid(currentState):
                vaildStates += 1

                node = BST.Node(currentState.toString(currentState))

    def runGenTree(self):
        graph = self.generateDecisionTree(self)

    def addLeadingZeroes(self, num=""):
        while num.__len__() < 4:
            num = "0" + num
        return num

    def generateDecisionTree(self):
        graph = Graph

        currentState = State
        validStates = 0

        for i in range(self.permutations):
            currentState = State.newState(currentState, self.addLeadingZeroes(str(i) + str(NUM_STATES)))
            print("CS: ", currentState)

            if currentState.IsValid(currentState):
                node = graph.generateSingleNode(graph, str(currentState))
