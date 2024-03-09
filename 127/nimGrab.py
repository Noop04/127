# Anoop Boyal             9/28/22
# Assignment 3



import random 
print("Welcome to NIMGRAB!")
print()

print("By: Anoop Boyal")
print("[COM S 127 D]")
print()

# Constant values
NUM_ITEMS_LOW = 4
NUM_ITEMS_HIGH = 8
NUM_TO_TAKE_LOW = 1
NUM_TO_TAKE_HIGH = 3


# Game flow variables
game0ver = False
currentTurn = 0 # 0 = human, 1 = computer NOTE: Alternate between turns 0 and 1 to play the game






while game0ver == False:
    choice = input("What would you like to do [p]lay, [i]nstructions, [q]uit? ")

    if choice == 'q':
        print("Goodbye!")
        quit()

    elif choice == 'i':
        print("There is an amount of an items, you take turns taking an amount between 1-3, if you take the last item you lose.")
        
        
    elif choice == 'p':
        numitems = random.randint(NUM_ITEMS_LOW, NUM_ITEMS_HIGH)
        
        print(numitems," items")
        s = numitems
        while s>0:
            print("|",end="")
            s -= 1
        print()

        while numitems>0:
            if currentTurn == 0:
                print("HUMAN TURN: ")
            a = int(input("How many will you take: "))
 

            if a > 3 or a < 1:
                print("Enter a valid take 1-3. ")
                print("Their are ",numitems," left.")
                continue
        

            numitems -= a
            print("their are now ", numitems, " items")

            s = numitems
            while s>0:
                print("|",end="")
                s -= 1
            print()

            if numitems <= 0:
                print("You have took the last Item Therefore computer has won the game!")
                break


            currentTurn += 1


            while currentTurn == 1:
                print("Computers Turn: ")


                if numitems == 3:
                    computerTake = 2
                    numitems -= computerTake
                    print("Their are ", numitems,"Items, Computer has decided to take ", computerTake)

                elif numitems == 2:
                    computerTake = 1
                    numitems -= computerTake
                    print("Their are ", numitems,"Items, Computer has decided to take ", computerTake)

                elif numitems == 1:
                    print("The Computer took the last Item Therfore Human has won.")
                    numitems-=1

                if numitems > 3:
                    computerTake = random.randint(NUM_TO_TAKE_LOW, NUM_TO_TAKE_HIGH)
                    numitems -= computerTake
                    print("Their are ", numitems,"Items, Computer has decided to take ", computerTake)
                print()

                s = numitems
                while s>0:
                    print("|",end="")
                    s -= 1
                print()

                currentTurn -= 1






else:
    print("Enter a valid option.")


   
