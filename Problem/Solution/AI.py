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

        currentState = St
        vaildStates = 0

        for i in range(self.permutations):

            #state = new State(addLeadingZeros(Integer.toString(i, NUM_STATES)));
            #this is how we would deal with it in java. so how do we toString(i, NUM_STATES) in python?
            #NUM_STATES is the radix for the function.
            # how do we implement a radix or similar
            currentState.newState(currentState,self.addLeadingZeroes(self, str(i % NUM_STATES)))
            if currentState.isValid(currentState):
                vaildStates += 1
                nextStep = St
                for j in range(self.permutations):
                    nextStep.newState(nextStep, self.addLeadingZeroes(self, str(j % NUM_STATES)))

                    if nextStep.isValid(nextStep) and currentState.isValidNextStep(currentState, nextStep):
                        currentState.beingMoved(currentState, nextStep)
                        if currentState.state not in self.poss_States:
                            self.poss_States.append(currentState.state.copy())


        print("Number of possibilities: ", self.permutations)
        print("Number of valid states: ", vaildStates)

        print(self.poss_States)

    def runGenTree(self):
        graph = self.generateDecisionTree(self)

    def addLeadingZeroes(self, num=""):
        if num.isnumeric():
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
