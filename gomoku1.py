#package to be imported
import numpy as np;
import random as rd;

#initializing the 2-d array 
board =[[" "]*3 for i in range(3)]
board = np.array(board)

#function for the human turn
def Human_Turn():
    x = int(input("Input The ROW where you want to put your stone between 1 and 3: "))
    y = int(input("Input The COL where you want to put your stone between 1 and 3: "))
    board[x-1][y-1]= "O"
    Print_Board()

#function for the machine turn 
def Random_Machine_Turn():
    print("machine turns")
    while(True):
        x=rd.randint(0, 2)
        y=rd.randint(0, 2)
        #checks if the position is already filled by human or not
        if(board[x-1][y-1]!=" "):
            continue
        else:
            board[x-1][y-1]="X"
            break
    Print_Board()
  

#function to display the board
def Print_Board():
    print(board)


Print_Board()
for i in range(4):
    Human_Turn()
    Random_Machine_Turn()
Human_Turn()
Print_Board()

print("*************************")
print("No more spot left. Game Ended.")
print("*************************")