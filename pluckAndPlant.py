from numpy import *
from random import randint

def main():
    gameBoard = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
    flower = [random.randint(0,4), random.randint(0,4)]
    gameBoard[flower[0]][flower[1]] = "F"
    kangaroo = [0,0]
    gameBoard[kangaroo[0]][kangaroo[1]] = "K"
    
    for i in gameBoard:
        print(i)
    
    gameBoard[kangaroo[0]][kangaroo[1]] = "0"
    hopToFlower(gameBoard)
    hopToPlantFlower(gameBoard)
        
def hopToFlower(board):
    colHop = int(input("Input the column you want to hop to (0-4): "))
    rowHop = int(input("Input the row you want to hop to (0-4): "))
    
    kangaroo = [rowHop,colHop]
    board[kangaroo[0]][kangaroo[1]] = "K"  
    
    for i in board:
        print(i)
    
    board[kangaroo[0]][kangaroo[1]] = "0"
        
def hopToPlantFlower(board):
    rowHop = int(input("Input the row you want to hop to plant the flower (0-4): "))
    colHop = int(input("Input the column you want to hop to plant the flower (0-4): "))
    
    flower = [rowHop,colHop]
    board[flower[0]][flower[1]] = "F"
    
    if(colHop + 1 <= 4):
        kangaroo = [rowHop, colHop + 1]
        board[kangaroo[0]][kangaroo[1]] = "K"
    elif(colHop - 1 >= 0):
        kangaroo = [rowHop, colHop-1]
        board[kangaroo[0]][kangaroo[1]] = "K"
        
    for i in board:
        print(i)
    
    
        
main()