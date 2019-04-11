from numpy import *
from random import randint
# The hidden game board that the user will not see 
gameBoard = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
#The visual game board that the user will see
usedGameBoard = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
for j in gameBoard:
    print(j)
    
ship = [random.randint(0,4), random.randint(0,4)]
print(ship)
gameBoard[ship[0]][ship[1]] = "*"

count = 0

while(count != 4):
    row = int(input("Please enter the row:"))
    col = int(input("Please enter the column:"))
    
    if(gameBoard[row][col] == "*"):
        print("Hit!")
        print("You win!")
        break
    else:
        print("Miss!")
        usedGameBoard[row][col] = "X"
        for i in usedGameBoard:
            print(i)
        count+=1
    
if(count == 4):
    print("You Lose!")
        
print("Game Over!")