from random import randint

choice_player = int()
play = "yes"
computerSc = int()
playerSc = int()        

while play  == "yes":
        
    choice_player = int(input("Choose:\n1) Rock \n2) Paper \n3) Scissors \n"))
    while choice_player > 3:
        choice_player = int(input("Choose:\n1) Rock \n2) Paper \n3) Scissors \n"))

    choice_computer = randint(1, 3)

    class logic:
        
        @staticmethod
        def win(x):
            print("You win")
            return x + 1            

        @staticmethod
        def lose(y):
            print("You lose")
            return y + 1

        @staticmethod
        def game(a, b, x, y):
            if a == b:
                print("Draw")
            if a == 1 and b == 2:
                logic.win(x)
            if a == 1 and b == 3:
                logic.lose(y)
            if a == 2 and b == 1:
                logic.lose(y)
            if a == 2 and b == 3:
                logic.win(x)
            if a == 3 and b == 1:
                logic.win(y)
            if a == 3 and b == 2:
                logic.lose(y)
    
            return x
            return y

    score = logic()
    playerSc = score.win(playerSc)
    computerSc = score.lose(computerSc)
    
    game = logic()
    game.game(choice_computer, choice_player, playerSc, computerSc)

    print("You chose: %d \nComputer chose: %d" %(choice_player, choice_computer))
    print("Score: You: %d Computer: %d" %(playerSc, computerSc))
    
    play = input("Again (yes/no)?\n")    

print("Final score: You: %d Computer: %d. Goodbye" %(playerSc, computerSc))
