from tkinter import * 

start = Tk()
start.title("Rock, Paper, Scissors")

canvas = Canvas(start, height=750, width=1250, bg="#4a4e54")
start.resizable(False, False)
canvas.create_text(650, 80, fill="white", text="Rock,\nPaper,\nScissors", anchor=N, font=("Helvetica", 100))

btnStart = Button(text="Play", font=("Helvetica", 30))
btnStart.configure(width=16, height=1, activebackground="#4a4e54")
btnStart_window = canvas.create_window(610,620, window=btnStart)

canvas.pack()
start.mainloop()