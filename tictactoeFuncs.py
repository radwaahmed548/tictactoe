# Project 3 - Tic-Tac-Toe Simulator
# 
# Name: Richard Rios, Nic Doorlay
# Instructor: S. Einakian 
# Section: 6


#prints the welcome screen
# none -> none
def Welcome(): 
    print("Welcome to Tic-Tac-Toe.\nYour goal is to get 3 in a row.\nyou will either pick X or O. X will go first.")
    players = int(input("Do you wish to play against a (1)computer, or with (2)Players? "))
    return players
   
# provides the board that shows 1-9 options
# none ->none 
def createBoard():
    board = []
    for i in range (9):
        board.append(str(i+1))
    return board  
   
# prints the game board for every turn
# list -> none
def printBoard(list):
    for i in range (0,6,3):
       print("",list[i],"|",list[i+1],"|",list[i+2])    
       print("------------")
    print("",list[6],"|",list[7],"|",list[8])

# user picks either X or O 
# I/O 
def pickLetter():
    letter = input("Choose X or O: ")
    while True:    
       if letter == "X" or letter == "O":
           break
       else:
           letter = input("Re-enter X or O: ")
    return letter

# gets the user inputted location and updates the board list
# string,list -> list
def getInput(letter, board):
    while True:
        location = int(input("Where would you like to place your letter (pick in range of 1-9): ")) - 1
        if (location < 0 or location > 8) or board[location] != " " :
            print("Invalid move! Location is already taken. Please try again.")
        else: 
            break
    board.pop(location)
    board.insert(location, letter)
    return board    
   
# checks the rows for a win
# list -> bool, string
def checkRows(board):
    if board[0] == board[1] == board[2] and board[0] != " ":
        return True, board[0]
    elif board[3] == board[4] == board[5] and board[3] != " ":
        return True, board[3]
    elif board[6] == board[7] == board[8] and board[6] != " ":
        return True, board[6]
    else:
        return False, board[0]   
   
# checks the columns for a win
# list -> bool, string
def checkCols(board):
    if board[0] == board[3] == board[6] and board[0] != " ":
        return True, board[0]
    elif board[1] == board[4] == board[7] and board[1] != " ":
        return True, board[1]
    elif board[2] == board[5] == board[8] and board[2] != " ":
        return True, board[2]
    else:
        return False, board[0]

# checks the diagonals for a win
# list -> bool, string
def checkDiags(board):
    if board[0] == board[4] == board[8] and board[0] != " ":
        return True, board[0]
    elif board[2] == board[4] == board[6] and board[2] != " ":
        return True, board[2]
    else: 
        return False, board[0]
  

# checks if the board is full
# list -> bool
def boardFull(board):
    boardNotFull = False
    for square in board:
        if square == " ":
            boardNotFull = True
            break
    if boardNotFull != True:
        return True
    else:
        return False

# checks for a win and prints a message accordingly 
# list -> bool  
def checkWin(board):
    if (checkRows(board))[0] == True:
        winner = checkRows(board)
        print("Congratulations, {}'s won!".format(winner[1]))
        return True
    elif (checkCols(board))[0] == True:
        winner = checkCols(board)
        print("Congratulations, {}'s won!".format(winner[1]))
        return True
    elif (checkDiags(board))[0] == True:
        winner = checkDiags(board)
        print("Congratulations, {}'s won!".format(winner[1]))
        return True
    elif boardFull(board) == True:
        print("It's a draw!")
        return True
    else:
        return False
 
# iterates the turn count
# none -> none
def turnCount(count):
    count += 1
    return count
