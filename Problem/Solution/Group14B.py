def main():
    start = ["hamster", "cat", "dog"]
    destination = []

    print("You are stranded on the side of the river with your three pets. "
          "\nHow are you going to get them across the river in a boat?"
          "\nThe boat can only hold yourself and one of the animals."
          "\nBe aware, the cat will attack the hamster in your absence and the dog would attack the cat.")

    choice = ""

    while choice != "cat":
        choice = input("Please select an animal to move: ")
        match choice:
            case "hamster":
                print("DISASTER!")
            case "dog":
                print("DISASTER!")
            case "cat":
                print("Correct choice")
                destination.append(start.pop(1))
                print("Start: ", start)
                print("Destination: ", destination)
            case default:
                print(choice, "was not an option!")

    bloop = True
    choice = ""
    while bloop:
        choice = input("Please select an animal to move: ")

        match choice:
            case "hamster":
                print("Correct choice")
                destination.append(start.pop(0))
                print("Start: ", start)
                print("Destination: ", destination)

                start.append(destination.pop(0))
                print("Cat would eat hamster! Take cat back")
                print("Start: ", start)
                print("Destination: ", destination)

                destination.append(start.pop(0))
                print("Dog would eat cat! Take Dog")
                print("Start: ", start)
                print("Destination: ", destination)

                destination.append(start.pop(0))
                print("Just the cat left...")
                print("Start: ", start)
                print("Destination: ", destination)

                bloop = False
                return


            case "dog":
                print("Correct choice")
                destination.append(start.pop(1))
                print("Start: ", start)
                print("Destination: ", destination)

                start.append(destination.pop(0))
                print("Dog would eat cat! Take cat")
                print("Start: ", start)
                print("Destination: ", destination)

                destination.append(start.pop(0))
                print("cat would eat hamster! Take hamster")
                print("Start: ", start)
                print("Destination: ", destination)

                destination.append(start.pop(0))
                print("Just the cat left...")
                print("Start: ", start)
                print("Destination: ", destination)
                bloop = False
                return

            case "cat":
                print(choice ,"is at destination")
            case default:
                print(choice, "was not an option!")



main()
