from tkinter import * 
from random import randint
from RpsGui import *

computerSc = 0
playerSc = 0
outcome = 0

def win():
    #print("You win.")
    global computerSc 
    computerSc += 1
    global outcome
    outcome = 1
    
    
def lose():
    #print("You lose.")
    global playerSc
    playerSc += 1
    global outcome
    outcome = 2
    
    
def rock(a):
    if a == 1:
        #print("Draw.")
        pass
    if a == 2:
        lose()
    if a == 3:
        win()
    
def paper(a):
    if a == 1:
        win()
    if a == 2:
        #print("Draw.")
        pass
    if a == 3:
        lose()
    
def scissors(a):
    if a == 1:
        lose()
    if a == 2:
        win()
    if a == 3:
        #print("Draw.")
        pass

def gameLogic(a):
    playerCh = a
        
    gameLogic.computerCh = randint(1,3)

    if gameLogic.computerCh == 1:
        rock(playerCh)
    if gameLogic.computerCh == 2:
        paper(playerCh)
    if gameLogic.computerCh == 3:
        scissors(playerCh)
    
    gameLogic.score = "Score: Player %d - %d Computer" %(playerSc, computerSc)
    
    global outcome
    gameLogic.outcome = outcome
    outcome = 0

    return gameLogic.score