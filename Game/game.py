from random import randint
from RpsGui import *

playerCh = int()
computerSc = 0
playerSc = 0        

def win():
    print("You win.")
    global playerSc 
    playerSc += 1
    return playerSc
    
def lose():
    print("You lose.")
    global computerSc
    computerSc += 1
    return computerSc

def rock(a):
    if a == 1:
        print("Draw.")
    if a == 2:
        lose()
    if a == 3:
        win()
    
def paper(a):
    if a == 1:
        win()
    if a == 2:
        print("Draw.")
    if a == 3:
        lose()
    
def scissors(a):
    if a == 1:
        lose()
    if a == 2:
        win()
    if a == 3:
        print("Draw.")

def gameLogic(a):
        global playerCh
        playerCh = a
        
        computerCh = randint(1,3)

        if computerCh == 1:
            rock(playerCh)
        if computerCh == 2:
            paper(playerCh)
        if computerCh == 3:
            scissors(playerCh)  
        
        print(playerSc, computerSc)