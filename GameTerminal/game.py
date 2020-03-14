from random import randint

playerCh = int()
play = "yes"
computerSc = 0
playerSc = 0        

while play  == "yes":
        
    playerCh = int(input("Choose:\n1) Rock \n2) Paper \n3) Scissors \n"))
    while playerCh > 3:
        playerCh = int(input("Choose:\n1) Rock \n2) Paper \n3) Scissors \n"))

    computerCh = randint(1, 3)


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

    if computerCh == 1:
        rock(playerCh)
    if computerCh == 2:
        paper(playerCh)
    if computerCh == 3:
        scissors(playerCh)       

   

    print("You chose: %d \nComputer chose: %d" %(playerCh, computerCh))
    print("Score: You: %d Computer: %d" %(playerSc, computerSc))
    
    play = input("Play again (yes/no)?\n")

print("Final score: You: %d Computer: %d. Goodbye" %(playerSc, computerSc))
