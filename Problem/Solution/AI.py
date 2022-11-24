from CONSTANTS import *
from DataFactory import DataFactory
from State import State as St



class AI:
    startState = None
    endState = None
    poss_States = []
    bst = None
    permutations = 0
    df = None

    def AI(self):
        self.init(self)

    def init(self):
        self.startState = St
        self.endState = St
        self.startState.State(self.startState, 0, 0, 0, 0)
        self.endState.State(self.endState, 2, 2, 2, 2)
        self.permutations = int(pow(NUM_STATES, NUM_OBJECTS))
        self.df = DataFactory
        self.df.__init__(self.df)

    def run(self):

        currentState = St
        validStates = 0
        ##TODO: consider using binSearch or decision tree
        for i in range(self.permutations):

            currentState.newState(currentState, self.df.addLeadingZeroes(self.df, self.df.strFromBase(self.df, i, NUM_STATES)))
            if currentState.isValid(currentState):
                validStates += 1
                nextStep = St
                for j in range(self.permutations):
                    nextStep.newState(currentState, self.df.addLeadingZeroes(self.df, self.df.strFromBase(self.df, j, NUM_STATES)))


                    if nextStep.isValid(nextStep) and currentState.isValidNextStep(currentState, nextStep):
                        currentState.beingMoved(currentState, nextStep)
                        if currentState.state not in self.poss_States:
                            self.poss_States.append(currentState.state)
        ##TODO: sort out finding the right path from poss_States

        print("Number of possibilities: ", self.permutations)
        print("Number of valid states: ", validStates)

        print(self.poss_States)

