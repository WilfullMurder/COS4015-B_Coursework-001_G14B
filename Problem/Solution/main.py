def main():
    start = ["hamster", "cat", "dog"]
    destination = []

    runIntro(start, destination)

    bloop = True
    choice = ""
    while bloop:
        choice = input("Please select an animal to move: ")

        match choice:
            case "hamster":
                print("Correct choice")
                hamsterSelection(start, destination, 0)

                break

            case "dog":
                print("Correct choice")
                dogSelection(start, destination, 1)

                break

            case "cat":
                print(choice, "is at destination")
            case default:
                print(choice, "was not an option!")

    moveCat(start, destination, True)

    if input("Try again? y/n") == "n":
        bloop = False
        return

    main()


def runIntro(start=[], dest=[]):
    print("You are stranded on the side of the river with your three pets. "
          "\nHow are you going to get them across the river in a boat?"
          "\nThe boat can only hold yourself and one of the animals."
          "\nBe aware, the cat will attack the hamster in your absence and the dog would attack the cat.")

    choice = ""
    ##first choice must always be cat
    while choice != "cat":
        choice = input("Please select an animal to move: ")
        match choice:
            case "hamster":
                print("DISASTER!! \ntry again")
            case "dog":
                print("DISASTER!! \ntry again")
            case "cat":
                print("Correct choice")
                moveAnimal(start, dest, 1)
                printValues(start, dest)
            case default:
                print(choice, "was not an option!")


def moveAnimal(start=[], dest=[], startI=0):
    dest.append(start.pop(startI))


def hamsterSelection(start=[], dest=[], i=0):
    #TODO:work out how to separate the hamster and dog selection so they can be called in either order

    if i < 1:
        moveAnimal(start, dest, 0)


    if start == ["cat", "hamster"] or start == ["hamster", "cat"]:
        print("cat would attack hamster!!")
        moveAnimal(start, dest, 0)


    elif dest == ["cat", "hamster"] or dest == ["hamster", "cat"]:
        print("cat would attack hamster!!")
        moveCat(dest, start, False)
        dogSelection(start, dest, i)

    else:
        moveAnimal(start, dest, 0)
        printValues(start, dest)

    printValues(start, dest)






def dogSelection(start=[], dest=[], i=0):
    #TODO:work out how to separate the hamster and dog selection so they can be called in either order
    if i > 0:
        moveAnimal(start, dest, i)
        printValues(start, dest)

    if start == ["cat", "dog"] or start == ["dog", "cat"]:
        print("Dog would attack cat! Take dog")
        moveAnimal(start, dest, 0)
        printValues(start, dest)
    elif dest == ["cat", "dog"] or dest == ["dog", "cat"]:
        print("Dog would attack cat! Take cat")
        moveCat(dest, start, False)
        printValues(start, dest)
        hamsterSelection(start, dest, i)














def moveCat(start=[], dest=[], final=False):
    moveAnimal(start,dest,0)
    if final:
        print("Only the cat remains...")
    printValues(start, dest)


def printValues(start=[], dest=[]):
    print("Start: ", start)
    print("Destination: ", dest)

main()
