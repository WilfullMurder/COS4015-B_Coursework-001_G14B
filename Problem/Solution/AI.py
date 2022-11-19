from State import State
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris, load_boston, make_classification
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
        X, t = make_classification(100, 5, n_classes=2, shuffle=True, random_state=10)
        X_Train, X_Test, t_train, t_test = train_test_split(X, t, test_size=0.3, shuffle=True, random_state=1)
        model = tree.DecisionTreeClassifier()
        model = model.fit(X_Train, t_train)

        predictedVal = model.predict(X_Test)
        print(predictedVal)

        tree.plot_tree(model)
        zeroes = 0
        ones = 0
        for i in range(0, len(t_train)):
            if t_train[i] == 0:
                zeroes +=1
            else:
                ones += 2

        print(zeroes)
        print(ones)

        val = 1 - (zeroes/70)*(zeroes*70) + (ones/70)*(ones/70)
        print("Gini: ", val)

        match = 0
        Unmatch = 0

        for i in range(30):
            if predictedVal[i] == t_test[i]:
                match +=1
            else:
                Unmatch += 1

        accuracy = match / 30
        print("Accuracy: ", accuracy)


