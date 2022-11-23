import random

import BST
from AI import AI
from DataFactory import DataFactory
from Graph import Graph
from State import State


def main():
    testDataFactory()


def testBST():
    bst = BST.BinarySearchTree
    bst.__init__(bst, "0000")
    print(bst.root)
    print(bst.tree)
    print(bst.heap)


def testGraph():
    g = Graph
    g.__init__(g)
    g.generateNodes(g)


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
    print(df.getData(df))

    l = []
    for i in range(len(df.getData(df))):
        l.append(df.addLeadingZeroes(df.strFromBase(df, i, 3)))
        print("Data[", i, "], base-3 format: ", l[i])

    l = []
    for i in range(1000):
        l.append(df.addLeadingZeroes(df.strFromBase(df, i, 16)))
        print("Data[", i, "], HEX format: ", l[i])



def testAI():
    ai = AI
    ai.AI(ai)
    ai.run(ai)


main()
