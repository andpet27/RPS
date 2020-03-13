from tkinter import * 

start = Tk()
start.title("Rock, Paper, Scissors")

canvas = Canvas(start, height=750, width=1250, bg="#4a4e54")
start.resizable(False, False)
canvas.create_text(650, 80, fill="white", text="Rock,\nPaper,\nScissors", anchor=N, font=("Helvetica", 100))





canvas.pack()
start.mainloop()