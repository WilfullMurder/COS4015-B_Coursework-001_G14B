class State:
    student = 0
    hamster = 0
    cat = 0
    dog = 0

    def State(self, student=0, hamster=0, cat=0, dog=0):
        self.student = student
        self.hamster = hamster
        self.cat = cat
        self.dog = dog

    def newState(self, state=""):
        self.student = int(state[0])
        self.hamster = int(state[1])
        self.cat = int(state[2])
        self.dog = int(state[3])

    def isValid(self):
        # Only 2 obj on boat simultaneously
        boatCount = 0
        boatCount = (((self.student == 1) if 1 else 0) +
                     ((self.hamster == 1) if 1 else 0) +
                     ((self.cat == 1) if 1 else 0) +
                     ((self.dog == 1) if 1 else 0))
        if boatCount > 2:
            return False

        if (self.cat == self.dog) or (self.cat == self.hamster) and self.cat != self.student:
            ##cat cannot be left alone with hamster or dog
            return False

        if (self.hamster == 1 or self.cat == 1 or self.dog == 1) and self.student != 1:
            ##student must be present in boat
            return False

        ##default to True
        return True

    def isValidNextStep(self, nextState=None):
        ##obj can only traverse a singular unit
        if abs(self.student - nextState.student) > 1 or \
                abs(self.hamster - nextState.hamster) > 1 or \
                abs(self.cat - nextState.cat) > 1 or \
                abs(self.dog - nextState.dog) > 1:
            return False

        ##only the student may move obj
        if self.cat != nextState.cat and (self.student != self.cat or nextState.student != nextState.cat):
            return False
        if self.hamster != nextState.hamster and (self.student != self.hamster or nextState.student != nextState.hamster):
            return False
        if self.dog != nextState.dog and (self.student != self.dog or nextState.student != nextState.dog):
            return False

        return True

    def beingMoved(self, nextState=None):
        if self.cat != nextState.cat:
            return "Cat"
        if self.chicken != nextState.chicken:
            return "Hamster"
        if self.dog != nextState.dog:
            return "Dog"

        return ""



    def toString(self):
        return str(self.student) + str(self.hamster) + str(self.cat) + str(self.dog)

    def printVisual(self):
        pass
