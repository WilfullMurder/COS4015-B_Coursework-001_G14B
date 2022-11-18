
import random

from AI import AI
from DataFactory import DataFactory
from State import State


def main():
    testDataFactory()





def testState():
    s = State
    s.State(s, 0, 0, 0, 0)
    print(s.toString(s))
    print(s.isValid(s))
    s.newState(s, "0111")
    print(s.toString(s))
    print(s.isValid(s))
    s.newState(s, "0101")
    print(s.toString(s))
    print(s.isValid(s))
    s.newState(s, "1012")
    print(s.toString(s))
    print(s.isValid(s))
    s.printVisual(s)

def testDataFactory():
    numStates = 3
    numObjects = 4
    permutations = int(pow(numStates, numObjects))
    print("Number of permutations: ", permutations)

    df = DataFactory
    df.__init__(df)
    print("Length: ", len(df.data))
    for i in df.data:
        print(i)

main()
