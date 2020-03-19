from tkinter import * 
from game import *
from random import randint

start = Tk()
start.title("Rock, Paper, Scissors")

canvasStart = Canvas(start, height=700, width=1250, bg="#4a4e54")
start.resizable(False, False)
canvasStart.create_text(650, 80, fill="white", text="Rock,\nPaper,\nScissors", anchor=N, font=("Helvetica", 100))

def callCanvasGame():
    start.destroy()
    game = Tk()
    game.title("Rock, Paper, Scissors")
    callCanvasGame.canvasGame = Canvas(game, height=700, width=1250, bg="#4a4e54")
    game.resizable(False,False)
    scoreTxt = callCanvasGame.canvasGame.create_text(600, 100, fill="white", text=("Score: Player %d - %d Computer" %(playerSc, computerSc)), anchor=S, font=("Helvetica", 40))

    imgRPS = PhotoImage(file='imgs/RPS.PNG')
    logoRPS = imgRPS.subsample(1, 1)
    computerChoice = Label(callCanvasGame.canvasGame, image=logoRPS, bg="#4a4e54")
    callCanvasGame.canvasGame.create_window(600, 305, window=computerChoice)
    winLoseTxt = callCanvasGame.canvasGame.create_text(600, 540, fill="white", text="", anchor=S, font=("Helvetica", 25))

    imgRock = PhotoImage(file='imgs/Rock.png')
    logoRock = imgRock.subsample(2, 2)
    btnRock = Button(command=lambda:[gameLogic(1), scoreUpdate(), computerChImg(), outcome()])
    btnRock.configure(image=logoRock, width=100, height=100, activebackground="#a3a29d")
    btnRock_window = callCanvasGame.canvasGame.create_window(400, 610, window=btnRock)    

    imgPaper = PhotoImage(file='imgs/Paper.png')
    logoPaper = imgPaper.subsample(2, 2)
    btnPaper = Button(command=lambda:[gameLogic(2), scoreUpdate(), computerChImg(), outcome()])
    btnPaper.configure(image=logoPaper, width=100, height=100, activebackground="#a3a29d")
    btnPaper_window = callCanvasGame.canvasGame.create_window(600, 610, window=btnPaper)

    imgScissors = PhotoImage(file='imgs/Scissors.png')
    logoScissors = imgScissors.subsample(2, 2)
    btnScissors = Button(command=lambda:[gameLogic(3), scoreUpdate(), computerChImg(), outcome()])
    btnScissors.configure(image=logoScissors, width=100, height=100, activebackground="#a3a29d")
    btnScissors_window = callCanvasGame.canvasGame.create_window(800, 610, window=btnScissors)

    def scoreUpdate():
        callCanvasGame.canvasGame.itemconfigure(scoreTxt, text=gameLogic.score)

    def computerChImg():
        if gameLogic.computerCh == 1:
            computerChoice.configure(image=imgRock)
            computerChoice.update()
        if gameLogic.computerCh == 2:
            computerChoice.configure(image=imgPaper)
            computerChoice.update()
        if gameLogic.computerCh == 3:
            computerChoice.configure(image=imgScissors)
            computerChoice.update()
    
    def outcome():
        
        if gameLogic.outcome == 1:
            callCanvasGame.canvasGame.itemconfigure(winLoseTxt, text="You lose.")
        if gameLogic.outcome == 2:
            callCanvasGame.canvasGame.itemconfigure(winLoseTxt, text="You win.")
        if gameLogic.outcome == 0:
            callCanvasGame.canvasGame.itemconfigure(winLoseTxt, text="Tie.")
    
    callCanvasGame.canvasGame.pack()
    game.mainloop()

       
btnStart = Button(text="Play", font=("Helvetica", 30), command=callCanvasGame)
btnStart.configure(width=16, height=1, activebackground="#a3a29d")
btnStart_window = canvasStart.create_window(610, 620, window=btnStart)

canvasStart.pack()
start.mainloop()