#prints the welcome screen
def Welcome(): 
    print("Welcome to Tic-Tac-Toe.\nYour goal is to get 3 in a row.\nyou will either pick X or O. X will go first.")
    players = int(input("Do you wish to play against a (1)computer, or with (2)Players? "))
    return players

# provides the board that shows 1-9 options
def createBoard():
    board = []
    for i in range (9):
        board.append(str(i+1))
    return board  

# prints the game board for every turn
def printBoard(list):
    for i in range (0,6,3):
       print("",list[i],"|",list[i+1],"|",list[i+2])    
       print("------------")
    print("",list[6],"|",list[7],"|",list[8])



def pickLetter():
    letter = input("Choose X or O: ")
    while True:
       if letter == "X" or letter == "O":
           break
       else:
           letter = input("Re-enter X or O: ")
    return letter

# it is used to detect input and see whether the input place is suitable or not
def getInput(letter,board):
    while True:
        location = int(input("Where would you like to place your letter(pick in range 1-9):")) - 1
        if (location < 0 or location > 8 ) or board[location] != " " :
            print("Invalid Move! Location is already taken. Please try again.")
            else:
                break
            board.pop(location)
            board.insert(location,letter)
            return board
def checkDiags(board):
    if board[0] == board[4] == board[8] and board[0] != " ":
        return True, board[0]
    elif board[2] == board[4] == board[6] and board[2] != " ":
        return True, board[2]
    else:
        return False, board[0]

def checkRows(board):
    if board[0] == board[1] == board[2] and board[2] !=" ":
       return True,board[0]
    elif board[3]==board[4] == board[5] and board[5] !=" " :
        return True,board[3]
    elif board[6]==board[7]==board[8] and board[8] != " " :
        return True,board[6]
    else:
        return False,board[0]

#to check the cols to detect whether the player wins or no
def checkCols(board):
    if board[0] == board[3] == board[6] and board[0] !=" ":
        return True,board[0]
    elif board[1] == board[4] == board[7] and board[1] !=" ":
        return true,board[1]
    else board[2] == board[5] == board[8] and board[2] !=" ":
        return true,board[2]
    else:
        return False,board[0]

#function to check the board is full or not
def boardFull (board):
    boardNotFull = False
    for square in board:
        if square == " ":
            boardNotFull = True
            break
    if boardNotFull != True:
        return True
    else:
        return False
def checkWin(board):
    if(checkCols(board))[0]== True:
        winner = checkCols(board)
        print("Congratulations,{}'s won".format(winner[1]))
         return 1
    elif(checkRows(board))[0]== True:
        winner = checkRows(board)
        print("Congratulations,{}'s won".format(winner[1]))
         return 1
    elif(checkDiags(board))[0]== True:
        winner = checkDiags(board)
        print("Congratulations,{}'s won".format(winner[1]))
         return 1
    elif boardFull(board)==True:
        print("It's draw")
        return True
    else
       return False





# iterates the turn count
def turnCount(count):
    count += 1
    return count


