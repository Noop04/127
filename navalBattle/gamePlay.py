# Anoo- Boyal             11-19-2022
# Assignment #6 Naval Battle

import gameBoard1
import gameInput

def _humanTurn(humanGameBoard, targetBoard, computerGameBoard, numComputerTargets):
    """This function controls what happens when it is the human's turn.

    Args:
        humanGameBoard (list of lists): Contains the 'bottom part' of the gameboard - where the 'ships' are placed.

        targetBoard (list of lists): Contains the 'top part' of the gameboard - where the hits/ misses against the computer go. 
        Only the human needs one.

        computerGameBoard (list of lists): Contains the 'bottom part' of the gameboard - where the 'ships' are placed.

        numComputerTargets (int): The number of computer targets remaining.
    
    Returns:
        list of lists, list of lists, list of lists, int: All of the relevant gameboards and the number of computer targets remaining.
    """
    # TODO: Complete the logic below so that the human can take a turn attacking the computer. (1 pt.)

    # Print out that it's the human's turn, as well as the targetBoard and humanGameBoard.
    print("----------------------------------------------------------")
    print("ENEMY BOARD:")
    gameBoard1.printBoard(targetBoard, 10, 10)
    print()
    print("YOUR BOARD:")
    gameBoard1.printBoard(humanGameBoard, 10, 10)

    pass

    # Call gameInput.getHumanInput() to get input for where to attack (row and column).
    # Do input validation to make sure that the row/ column on the targetBoard is not already 'X' or 'O'
    # if it is, get new input.

    row, col = gameInput.getHumanInput()
        
    pass
    print("Your target ", "(", row, ",", col, ")" )
    # Print out the coordinates the human is targeting.
    pass



    if computerGameBoard[col][row] == '@':
        print("HIT")
        targetBoard[col][row] = 'X'
        numComputerTargets -= 1
    else:
        computerGameBoard[col][row] == '#'
        print("MISS")
        targetBoard[col][row] = 'O'


    # Check to see if the row and column on the computerGameBoard contains an '@'.
    # If it does, set it to 'X' on both computerGameBoard and targetBoard, print 'HIT',
    # and decrease the numComputerTargets variable by 1 (as that target has been hit).
    # Else, set that space on the computerGameBoard and targetBoard to 'O' and print 'MISS'.
    pass
    
    return humanGameBoard, targetBoard, computerGameBoard, numComputerTargets

def _computerTurn(humanGameBoard, numHumanTargets):
    """This function controls what happens when it is the computer's turn.

    Args:
        humanGameBoard (list of lists): Contains the 'bottom part' of the gameboard - where the 'ships' are placed.

        numHumanTargets (int): The number of human targets remaining.
    
    Returns:
        list of lists, int: All of the relevant gameboards and the number of human targets remaining.
    """
    # TODO: Complete the logic below so that the computer can take a turn attacking the human. (1 pt.)

    # Print out that it's the computer's turn.
    print("Computer Turn")
    pass

    # Call gameInput.getComputerInput() to get input for where to attack (row and column).
    # Do input validation to make sure that the row/ column on the targetBoard is not already 'X' or 'O'
    # if it is, get new input.
    row, col = gameInput.getComputerInput()
        
    pass

    # Print out the coordinates the computer is targeting.
    print("Computer target ", "(", row, ",", col, ")" )
    pass

    # Check to see if the row and column on the computerGameBoard contains an '@'.
    # If it does, set it to 'X' on the computerGameBoard, print 'HIT', 
    # and decrease the numHumanTargets variable by 1 (as that target has been hit).
    # Else, set that space on the computerGameBoard to 'O' and print 'MISS'.
    if humanGameBoard[col][row] == '@':
        print("HIT")
        humanGameBoard[col][row] = 'X'
        numHumanTargets -= 1
    elif humanGameBoard[col][row] == '.':
        print("MISS")
        humanGameBoard[col][row] = 'O'


    pass
    
    return humanGameBoard, numHumanTargets

def _printWinner(numComputerTargets, computerGameBoard):
    """This function prints out which player has won the game, depending on the numComputerTargets remaining.

    Args:
        numComputerTargets (int): The number of computer targets left. If there are none, the human wins. Else - the computer wins.

        computerGameBoard (list of lists): Contains the 'bottom part' of the gameboard - where the 'ships' are placed.
    """
    # TODO: Complete the logic below so that the player can see who won the game. (1 pt.)

    # Check if numComputerTargets is zero (0). If it is, print that the human has won.
    # Otherwise, print that the computer has won.
    if numComputerTargets == 0:
        print("You have Won the game")
        quit()
    else:
        print("The computer has won.")
    pass
    
    # Print the computer's gameboard for the player to see using the printBoard method of the gameBoard module.
    print(computerGameBoard)
    pass
    

    return

def runGame(humanGameBoard, targetBoard, computerGameBoard, numHumanTargets, numComputerTargets):
    """This function controls the flow of the game and switches turns between the human and the computer.

    Args:
        humanGameBoard (list of lists): Contains the 'bottom part' of the gameboard - where the 'ships' are placed.

        targetBoard (list of lists): Contains the 'top part' of the gameboard - where the hits/ misses against the computer go. 
        Only the human needs one.

        computerGameBoard (list of lists): Contains the 'bottom part' of the gameboard - where the 'ships' are placed.

        numHumanTargets (int): The number of human targets left.

        numComputerTargets (int): The number of computer targets left.
    """
    currentTurn = 0 # 0 = human, 1 = computer

    # play the game (HUMAN goes first)
    while numHumanTargets > 0 and numComputerTargets > 0:
        if currentTurn == 0:
            humanGameBoard, targetBoard, computerGameBoard, numComputerTargets = _humanTurn(humanGameBoard, targetBoard, computerGameBoard, numComputerTargets)
        else:
            humanGameBoard, numHumanTargets = _computerTurn(humanGameBoard, numHumanTargets)

        # switch whose turn it is
        currentTurn += 1
        currentTurn %= 2
    
    # print the winner once the game is over
    _printWinner(numComputerTargets, computerGameBoard)

    return
