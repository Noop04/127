# Anoop Boyal          10/26/22
# Assignment 5
import sys
import pickle
def initList():
    todoList = {}
    todoList["backlog"] = []
    todoList["todo"] = []
    todoList["in_progress"] = []
    todoList["in_review"] = []
    todoList["done"] = []
    return todoList
def saveList(todoList):
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "wb") as pickle_file:
            pickle.dump(todoList, pickle_file)
    except:
        print("ERROR (saveList): ./{0}.lst is not a valid file name!".format(listName))
        sys.exit()
def loadList():
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "rb") as pickle_file:
            todoList = pickle.load(pickle_file)
    except:
        print("ERROR (loadList): ./{0}.lst was not found!".format(listName))
        sys.exit()
    return todoList
def checkItem(item, todoList):
    itemFound = False
    keyName = ""
    index = -1
    for key,value in todoList.items():
        if item in todoList[key]:
            itemFound = True
            keyName = key + ' list'
            index = todoList[key].index(item)
    return itemFound, keyName, index
def addItem(item, toList, todoList):
    itemFound, keyName, index = checkItem(item, todoList)
    if itemFound == False:
        todoList[toList].append(item)
    else:
        print(item, "is already in the ",keyName)
    return todoList
def deleteItem(item, todoList):
    itemFound, keyName, index = checkItem(item, todoList)
    if itemFound == True:
        for value in todoList.values():
            if item in value:
                value.remove(item)
    else:
        print(item," was not found")
    return itemFound, todoList
def moveItem(item, toList, todoList):
    itemFound, todoList = deleteItem(item, todoList)
    addItem(item, toList, todoList)
    printTODOList(todoList)
    runApplication(todoList)
    return todoList
def printTODOList(todoList):
    for key in todoList.items():
        print(key)
    return None
def runApplication(todoList):
    while True:
        print("-----------------------------------------------------------------")
        choice = input("APPLICATION MENU: [a]dd to backlog, [m]ove item, [d]elete item, [s]ave list, or [q]uit to main menu?: ")
        print()
        if choice == "a":
            item = str(input("What would you like to add?: "))
            addItem(item, "backlog", todoList)
            printTODOList(todoList)
            pass
        elif choice == "m":
            while True:
                item = str(input("What item would you like to move?: "))
                itemFound, keyName, index = checkItem(item, todoList)
                if itemFound == True:
                    while True:
                        toList = input("where will this be moved: ")
                        while toList != 'b' and toList != 't' and toList != 'p' and toList != 'r' and toList != 'd':
                            toList = input("Where would you like to move this item [b]acklog [t]odo in_[p]rogress in_[r]eview [d]one?: ")
                        if toList == 'b':
                            todoList = moveItem(item, "backlog", todoList)
                        elif toList == 't':
                            todoList = moveItem(item, "todo", todoList)
                        elif toList == 'p':
                            todoList = moveItem(item, "in_progress", todoList)
                        elif toList == 'r':
                           todoList = moveItem(item, "in_review", todoList)
                        elif toList == 'd':
                            todoList = moveItem(item, "done", todoList)
                else:
                    print(item," was not found")
        elif choice == "d":
            item = str(input("What item would you like to delete?: "))
            deleteItem(item, todoList)
            printTODOList(todoList)
            pass
        elif choice == "s":
            saveList(todoList)
            print("Saving List...")
            print()
            printTODOList(todoList)
        elif choice == "q":
            print("Returning to MAIN MENU...")
            print()
            break
        else:
            print("ERROR: Please enter [a], [m], [d], [s], or [q].")
            print()
    return todoList
def main():
    taskOver = False
    print("The Ultimate TODO List")
    print()
    print("By: Anoop Boyal")
    print("[COM S 127 D]")
    print()
    while taskOver == False:
        print("-----------------------------------------------------------------")
        choice = input("MAIN MENU: [n]ew list, [l]oad list, or [q]uit?: ")
        print()
        if choice == "n": 
            todoList = initList()
            printTODOList(todoList)
            runApplication(todoList)
        elif choice == "l":
            todoList = loadList()
            printTODOList(todoList)
            runApplication(todoList)
        elif choice == "q":
            taskOver = True
            print("Goodbye!")
            print()
        else:
            print("Please enter [n], [l], or [q]...")
            print()
if __name__ == "__main__":
    main()