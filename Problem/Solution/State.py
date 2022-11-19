"""
LOCATION SYNTAX:
                |                |
                |                |
                |                |
                |                |
       ORIGIN   |    OBSTACLE    |    DESTINATION
                |                |
                |                |
                |                |
                |                |
        0               1               2
STATE SYNTAX: [STUDENT, HAMSTER, DOG, CAT]
"""





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

        if (self.cat == self.dog or self.cat == self.hamster) and self.cat != self.student:
            """cat cannot be left alone with hamster or dog"""
            return False

        if (self.hamster == 1 or self.cat == 1 or self.dog == 1) and self.student != 1:
            """student must be present in boat"""
            return False

        """default to True"""
        return True

    def isValidNextStep(self, nextState=None):
        """obj can only traverse a singular unit"""
        if abs(self.student - nextState.student) > 1 or \
                abs(self.hamster - nextState.hamster) > 1 or \
                abs(self.cat - nextState.cat) > 1 or \
                abs(self.dog - nextState.dog) > 1:
            return False

        """only the student may move obj"""
        if self.cat != nextState.cat and (self.student != self.cat or nextState.student != nextState.cat):
            return False
        if self.hamster != nextState.hamster and (
                self.student != self.hamster or nextState.student != nextState.hamster):
            return False
        if self.dog != nextState.dog and (self.student != self.dog or nextState.student != nextState.dog):
            return False

        return True

    def beingMoved(self, nextState=None):
        if self.cat != nextState.cat:
            return "Cat"
        if self.hamster != nextState.chicken:
            return "Hamster"

        if self.dog != nextState.dog:
            return "Dog"

        return ""

    def toString(self):
        """just straight ripped from java because it's a handy function for debug"""
        return str(self.student) + str(self.hamster) + str(self.cat) + str(self.dog)

    def printVisual(self):
        blank = "|               |"
        line = "|    {}    |"
        print("-"* 51)
        print(blank * 3)

        self.printLine(self,line, "Student", self.student)
        self.printLine(self,line, "Hamster", self.hamster)
        self.printLine(self,line, "Cat    ", self.cat)
        self.printLine(self,line, "Dog    ", self.dog)

        print(blank * 3)
        print("-"* 51)

    def printLine(self, line = "", value = "", location=0):
        blank = "|               |"

        match location:
            case 0:
                print(line.format(value) + blank + blank)
            case 1:
                print(blank + line.format(value) + blank)
            case 2:
                print(blank + blank + line.format(value))
            case 4:
                print(blank,blank,blank,blank)