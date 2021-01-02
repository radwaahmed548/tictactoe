# Project 3 - Tic-Tac-Toe Simulator
# 
# Name: Richard Rios, Nic Doorlay
# Instructor: S. Einakian 
# Section: 6


#make sure initial list is [" "," "," "," "," "," "," "," "," "] 
#spaces are necessary in the empty string for the board to print correctly

from tictactoeFuncs import *
from random import *

#plays the game
def tictactoe():
   turn = 0
   board = [" "," "," "," "," "," "," "," "," "]
   num_players = Welcome()
   print("The board positions are as follows:")
   printBoard(createBoard())
   print()
   if num_players == 1:
      computer = 0
      first = randint(1,2)
      if first == 1:
         player1 = 'X'
      else:
         player1 = 'O'
      printBoard(board)
      print()
      while True:
          if player1 == 'X' and turn%2 == 0:
                print("It's Player 1's (X's) turn!")
                getInput("X",board)
                print()
          elif player1 == 'O' and turn%2 == 0:
                   print("Computer's move:")
                   print() 
                   computer = randint(0,8)
                   while True:
                      if board[computer] != " ":
                          computer = randint(0,8)
                      else:
                          break                   
                   board[computer] = 'X'
          elif player1 == 'X' and turn%2 != 0:
                   print("Computer's move:")
                   print()
                   computer = randint(0,8)
                   while True:
                      if board[computer] != " ":
                          computer = randint(0,8)
                      else:
                          break
                   board[computer] = 'O'
          elif player1 == 'O' and turn%2 != 0:
                print("It's Player 1's (O's) turn!")
                getInput("O",board)
                print()
          printBoard(board)
          print()
          turn = turnCount(turn) 
          if checkWin(board) == True:
              break
   elif num_players == 2:
       player1_letter = pickLetter()
       print()
       printBoard(board)
       print()     
       while True:
          if player1_letter == 'X' and turn%2 == 0:
             print("It's Player 1's (X's) turn!")
             getInput('X',board)
             print()
          elif player1_letter == 'X' and turn%2 != 0:
             print("It's player 2's (O's) turn!")
             getInput('O',board)
             print()
          elif player1_letter == 'O' and turn%2 == 0:
             print("It's player 2's (X's) turn!")
             getInput('X',board)
             print()
          elif player1_letter == 'O' and turn%2 != 0:
             print("It's Player 1's (O's) turn!")
             getInput('O', board)
             print()
          printBoard(board)
          print()
          turn = turnCount(turn) 
          if checkWin(board) == True:
             break

if __name__=="__main__":
   tictactoe()
