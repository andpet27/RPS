from tkinter import * 
from game import *

start = Tk()
start.title("Rock, Paper, Scissors")

canvasStart = Canvas(start, height=750, width=1250, bg="#4a4e54")
start.resizable(False, False)
canvasStart.create_text(650, 80, fill="white", text="Rock,\nPaper,\nScissors", anchor=N, font=("Helvetica", 100))

def callCanvasGame():
    game = Tk()
    game.title("Rock, Paper, Scissors")
    canvasGame = Canvas(game, height=750, width=1250, bg="#4a4e54")
    game.resizable(False,False)
    

    canvasGame.create_text(600, 100, fill="white", text=("Score: Player %d - %d Computer" %(playerSc,computerSc)), anchor=S, font=("Helvetica", 40))


    canvasGame.pack()
    start.destroy()

btnStart = Button(text="Play", font=("Helvetica", 30), command=callCanvasGame)
btnStart.configure(width=16, height=1, activebackground="#a3a29d")
btnStart_window = canvasStart.create_window(610,620, window=btnStart)

canvasStart.pack()
start.mainloop()