from tkinter import * 
from game import *
from random import randint

start = Tk()
start.title("Rock, Paper, Scissors")

canvasStart = Canvas(start, height=750, width=1250, bg="#4a4e54")
start.resizable(False, False)
canvasStart.create_text(650, 80, fill="white", text="Rock,\nPaper,\nScissors", anchor=N, font=("Helvetica", 100))

def callCanvasGame():
    start.destroy()
    game = Tk()
    game.title("Rock, Paper, Scissors")
    canvasGame = Canvas(game, height=750, width=1250, bg="#4a4e54")
    game.resizable(False,False)

    btnRock = Button(text="Rock", font=("Helvetica", 10), command=lambda:gameLogic(1))
    btnRock.configure(width=10, height=1, activebackground="#a3a29d")
    btnRock_window = canvasGame.create_window(400, 700, window=btnRock)    

    btnPaper = Button(text="Paper", font=("Helvetica", 10), command=lambda:gameLogic(2))
    btnPaper.configure(width=10, height=1, activebackground="#a3a29d")
    btnPaper_window = canvasGame.create_window(600, 700, window=btnPaper)

    btnScissors = Button(text="Scissors", font=("Helvetica", 10), command=lambda:gameLogic(3))
    btnScissors.configure(width=10, height=1, activebackground="#a3a29d")
    btnScissors_window = canvasGame.create_window(800, 700, window=btnScissors)

    def score(a,b):
        print("Score: Player %d - %d Computer" %(a,b))

    canvasGame.create_text(600, 100, fill="white", text=score(playerSc, computerSc), anchor=S, font=("Helvetica", 40))

    canvasGame.pack()
    game.mainloop()
        

btnStart = Button(text="Play", font=("Helvetica", 30), command=callCanvasGame)
btnStart.configure(width=16, height=1, activebackground="#a3a29d")
btnStart_window = canvasStart.create_window(610, 620, window=btnStart)

canvasStart.pack()
start.mainloop()