# Anoop Boyal            10/11/22
# Assignment 4

import random
import sys

# GLOBAL CONSTANT VARIABLES
START_ROOM = 1
FINAL_ROOM = 7
START_HEALTH = 10

def story1():
    print("You can sense a magical shop nearby.")

def story2():
    print("You sense a precence of something it could be dangerous.")

monsterHP = 3
goldAmount = 0


def combat(health, killedmonster):
    monsterHP = 3
    print("There is a Slime Monster! Will you fight or run away?")
    print()
    print("Health: ", health)
    while killedmonster == False:
        f = input("[a]ttack or [r]un?: ")
        print("--------------------------------------------------------------------")
        if f == 'a':
            print("Health: ", health)
            monsterHP -= 1
            health -= 1 
            print("You hit the monster its now has {0} hp.".format(monsterHP))
            print("The monster hit you back you now have {0} hp.".format(health))
            print()
            if monsterHP == 0:
                print("You killed the monster!")
                killedmonster = True        
            elif health == 0:
                print("The Monster has killed you!")
                gameOver = True
        elif f =='r':
            print()
            print("Which way will you go to escape?: ")
            break
        else:
            print("[a]ttack or [r]un?: ")
    return health, killedmonster
       


def shop(goldAmount, health):
    print()
    print("You have {0} hp".format(health))
    shopS = input("Welcome to the magical shop, would you like to refill your health back to ten hp with ten gold? [y]es or [n]o: ")
    if shopS == 'y' and goldAmount >= 10:
        health = 10
        goldAmount = goldAmount - 10
        print("You now have {0} hp!".format(health))
        
    elif goldAmount < 10:
        print("you only have ", goldAmount,", and you need at least 10.")
    elif shopS == 'n':
        print("You have ",health," hitpoints")
    return health, goldAmount

def room1(goldAmount, visited_room, health):
    if visited_room == False:
        gold = 10 # This is the amount of gold the room contains.
        print("--------------------------------------------------------------------")

        print("room 1")
        print()
        print("The room has", gold, "gold pieces in it...")
        goldAmount += gold
        print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
        print()
        
        
        # Mark the room as 'visited'
        visited_room = True
    else:
        print("--------------------------------------------------------------------")
        print("Room 1")
        print()
        print("You have already visited this room before...")
        print()
        print(goldAmount)

   
    direction = input("[n] [s]?: ")
    while direction != "n" and direction != "s":
        print("Invalid input...")
        direction = input("[n] [s]?: ")
    
    roomChoice = -1 
    if direction == "n":
        roomChoice = 2
    elif direction == "s":
        roomChoice = main()
 
    
  
    return roomChoice, goldAmount, visited_room, health


def room2(goldAmount, visited_room, health):
    if visited_room == False:
        gold = 5 # This is the amount of gold the room contains.
        print("--------------------------------------------------------")
        print()
        print("room 2")
        story2()
        print()
        print("The room has", gold, "gold pieces in it...")
        goldAmount += gold
        print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
        print()

        visited_room = True
    else:
        print("--------------------------------------------------------------------")
        print("Room 2")
        print()
        print("You have already visited this room before...")
        print()
        print(goldAmount)
    # NOTE: Replace this code before the 'return' statement with the 'direction' function created in the 'room1' function above.
    direction = input("[n] [s]?: ")
    while direction != "n" and direction != "s":
        print("Invalid input...")
        direction = input("[n] [s]?: ")
    
    roomChoice = -1
    if direction == "n":
        roomChoice = 3
    elif direction == "s":
        roomChoice = 1
    return roomChoice, goldAmount, visited_room, health

def room3(goldAmount, visited_room3, health):
    if visited_room3 == False:
        print()
        print("--------------------------------------------------------------------")
        gold = 10
        goldAmount += gold
        print("room 3")
        print()
        story1()
        print()
        print("This room had {0} gold, after taking the gold you have {1} in your possecion.".format(gold,goldAmount))
        print()
        visited_room3 = True
        direction = input("[n] [s] [e] [w]?: ")
        while direction != "n" and direction != "s" and direction != "e" and direction != "w":
            print("Invalid input...")
            
    else:
        print("--------------------------------------------------------------------")
        print("Room 3")
        print()
        print("You have already visited this room before.")
        direction = input("[n] [s] [e] [w]?: ")
        print()
        print(goldAmount)
        while direction != "n" and direction != "s" and direction != "e" and direction != "w":
            print("Invalid input...")
            direction = input("[n] [s] [e] [w]?: ")
    
    roomChoice = -1
    if direction == "n":
        roomChoice = 6
    elif direction == "s":
        roomChoice = 2
    elif direction == 'e':
        roomChoice = 5
    elif direction == 'w':
        roomChoice = 4
    return roomChoice, goldAmount, visited_room3, health

def room4(goldAmount, visited_room4, health, killedmonster):
    print("Health: ", health)
    print("----------------------------------------------------------------")
    print()
    print("Room 4")

    if killedmonster == False:
        health, killedmonster = combat(health, killedmonster)
    
    if visited_room4 == False and killedmonster == True:
            gold = 5
            goldAmount += gold
            print()
            print("This room had {0} gold, after taking the gold you have {1} gold in your possession.".format(gold,goldAmount)) 
            visited_room4 = True

    elif visited_room4 == True:
        print("--------------------------------------------------------------------")
        print("Room 4")
        print()
        print("You have already visited this room before.")
        print(goldAmount)
 
    print()
    direction = input("[e]?: ")
    while direction != "e":
        print("Invalid input...")
        direction = input("[e]?: ")
    roomChoice = -1
    if direction == 'e':
        roomChoice = 3
    return roomChoice, goldAmount, visited_room4, health, killedmonster



def room5(goldAmount, visited_room5, health,  killedmonster):

    if killedmonster == False:
        health, killedmonster = combat(health, killedmonster)

    if visited_room5 == False and killedmonster == True:
        print("--------------------------------------------------------------------")
        print("Room 5")
        gold = 5
        goldAmount += gold
        print()
        print("This room had {0} gold, after taking the gold you have {1} in your possecion.".format(gold,goldAmount))
        visited_room5 = True
    else:
        print("--------------------------------------------------------------------")
        print("Room 5")
        print()
        print("You have already visited this room before.")

    direction = input("[w]")
    while direction != "w":
        print("Invalid input...")
        direction = input("[w]?: ")
    roomChoice = -1
    if direction == 'w':
        roomChoice = 3
    return roomChoice, goldAmount, visited_room5, health, killedmonster

def room6(goldAmount,health):
    print()
    print("--------------------------------------------------------------------")
    print("Room 6")
    health = shop(goldAmount, health)
    direction = input("[n] [s]?: ")
    while direction != "s" and direction != "n":
        print("Invalid input...")
        direction = input("[n] or [s]?: ")
    
    if direction =='n':
        roomChoice = 7
    if direction == "s":
        roomChoice = 3

    return roomChoice, goldAmount, health

    
# Main function
def main():
    # Set to 'True' when the game is over.
    gameOver = False

 
    START_GOLD = 0 # HINT: This is a 'constant' value. Notice how it is used to set/ reset the goldAmount value.
    goldAmount = START_GOLD
    currentRoom = START_ROOM
    visited_room1 = False 
    visited_room2 = False
    visited_room3 = False
    visited_room4 = False
    visited_room5 = False
    visited_room6 = False
    killedmonster = False 
    health = START_HEALTH
    print("Welcome to Dungeon Crawl...")
    print()

    print("By: Anoop Boyal")
    print("[COM S 127 D]")
    print()

    while gameOver == False:
        choice = input("MAIN MENU: [p]lay, [i]nstructions, or [q]uit?: ")
        print()
        if choice == "p": # (**"p" Section Tasks**)
            while currentRoom != FINAL_ROOM:
                if currentRoom == 1:
                    currentRoom, goldAmount, visited_room1, health = room1(goldAmount, visited_room1, health)
                elif currentRoom == 2:
                    currentRoom, goldAmount, visited_room2, health = room2(goldAmount, visited_room2, health)
                elif currentRoom == 3:
                    currentRoom, goldAmount, visited_room3, health = room3(goldAmount, visited_room3, health)                
                elif currentRoom == 4:
                    currentRoom, goldAmount,  visited_room4, health, killedmonster= room4(goldAmount,  visited_room4, health, killedmonster)
                elif currentRoom == 5:
                    currentRoom, goldAmount, visited_room5, health, killedmonster = room5(goldAmount, visited_room5, health, killedmonster)
                elif currentRoom == 6:
                    currentRoom, goldAmount, health = room6(goldAmount, health)
                else:
                    print("Error - currentRoom number", currentRoom, "does not correspond with available rooms")
                    sys.exit()

            print()
            print("You have escaped with", goldAmount, "gold from the dungeon!")
            print()
        elif choice == "i": # (**"i" Section Tasks**)
            print("Explore a dungeon to collect gold, beware of monsters!")
        elif choice == "q":
            gameOver = True
            print("Goodbye!")
        else:
            print()
            print("Please enter [p], [i], or [q]...")
            print()
if __name__ == "__main__":
    main()