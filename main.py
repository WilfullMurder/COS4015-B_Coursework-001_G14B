def main():
    start = ["hamster", "cat", "dog"] #this is O(1)
    destination = [] #this is O(1)

    #this is O(n) ~ I just googled it
    print("You are stranded on the side of the river with your three pets. "
          "\nHow are you going to get them across the river in a boat?"
          "\nThe boat can only hold yourself and one of the animals."
          "\nBe aware, the cat will attack the hamster in your absence and the dog would attack the cat.")

    choice = ""#this is O(1)

    while choice != "cat": # this is O(n)
        choice = input("Please select an animal to move: ") #this is O(n)
        match choice: #this is O(n^4)
            case "hamster":
                print("DISASTER!") #this is O(n)
            case "dog":
                print("DISASTER!") #this is O(n)
            case "cat":
                print("Correct choice") #this is O(n)
                destination.append(start.pop(1)) #this is O(n)
                print("Start: ", start) #this is O(n)
                print("Destination: ", destination) #this is O(n)
            case default:
                print(choice, "was not an option!") #this is O(n)

    bloop = True #this is O(1)
    choice = "" #this is O(1)
    while bloop: #this is O(n)
        choice = input("Please select an animal to move: ") #this is O(n)

        match choice: #this is O(n^4)
            case "hamster":
                print("Correct choice") #this is O(n)
                destination.append(start.pop(0)) #this is O(n)
                print("Start: ", start) #this is O(n)
                print("Destination: ", destination) #this is O(n)

                start.append(destination.pop(0)) #this is O(n)
                print("Cat would eat hamster! Take cat back") #this is O(n)
                print("Start: ", start) #this is O(n)
                print("Destination: ", destination) #this is O(n)

                destination.append(start.pop(0)) #this is O(n)
                print("Dog would eat cat! Take Dog") #this is O(n)
                print("Start: ", start) #this is O(n)
                print("Destination: ", destination) #this is O(n)

                destination.append(start.pop(0)) #this is O(n)
                print("Just the cat left...") #this is O(n)
                print("Start: ", start) #this is O(n)
                print("Destination: ", destination) #this is O(n)

                bloop = False
                return


            case "dog":
                print("Correct choice") #this is O(n)
                destination.append(start.pop(1))
                print("Start: ", start) #this is O(n)
                print("Destination: ", destination) #this is O(n)

                start.append(destination.pop(0))
                print("Dog would eat cat! Take cat") #this is O(n)
                print("Start: ", start) #this is O(n)
                print("Destination: ", destination) #this is O(n)

                destination.append(start.pop(0))
                print("cat would eat hamster! Take hamster") #this is O(n)
                print("Start: ", start) #this is O(n)
                print("Destination: ", destination) #this is O(n)

                destination.append(start.pop(0))
                print("Just the cat left...") #this is O(n)
                print("Start: ", start) #this is O(n)
                print("Destination: ", destination) #this is O(n)
                bloop = False
                return

            case "cat":
                print(choice ,"is at destination") #this is O(n)
            case default:
                print(choice, "was not an option!") #this is O(n)



main()