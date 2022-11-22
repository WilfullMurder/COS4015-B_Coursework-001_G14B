from CONSTANTS import *
from binarytree import tree, bst, heap, Node, build

from DataFactory import DataFactory
from State import State


class BinarySearchTree:
    tree = None
    heap = None
    root = None
    values = []

    def __init__(self, state=""):
        self.root = Node(state, None, None)
        df = DataFactory
        df.initData(df)
        s = State
        nextState = State


        for i in range(len(df.getData(df))):
            value = str(df.getData(df)[i])

            c = ""

            for j in value:
                if j.isnumeric():
                    c += j
            if c not in self.values:
                s.newState(s, c)
                if s.isValid(s):

                    self.values.append(c)
        print("Permutations: ", df.getData(df))
        print("Valid values: ", self.values)
        self.root = build(self.values)






    def genNode(self, node=None, data=None, i=0):
        if str(node.values) < str(data[i]):
            node.right = self.genNode(node.right, (data[i]), i + 1)
            return node.right
        elif str(node.values) > str(data[i]):
            node.left = self.genNode(node.left, (data[i]), i - 11)
            return node.left
        else:
            return node
