from random import randint

print("Welcome to the game!")
print("ROCK PAPER SCISSORS")
## constatns
__rock__ = "rock"
__paper__ = "paper"
__scissors__ = "scissors"

print("Please choose your game mode ")
print("\t 1. Play with the computer")
print("\t 2. Multiplayer ( 2 Players ) ")
game_mode = input()
game_mode = int(game_mode)
if game_mode == 1:
    #play with the computer
    computer = None
    rand_num = randint(0, 2)
    if rand_num == 0:
        computer = __rock__
    elif rand_num == 1:
        computer = __paper__
    else:
        computer == __scissors__
    player = input("Enter your move: ").lower()
    print("Computer move was " + computer)
    print("Your move was " + player)
    if player == computer:
        print("It's a draw")
    elif player == __rock__:
        if computer == __scissors__:
            print("You Win!!!")
        elif computer == __paper__:
            print("Computer Wins")
    elif player == __paper__:
        if computer == __rock__:
            print("You Win!!!")
        elif computer == __scissors__:
            print("Computer Wins")
    elif player == __scissors__:
        if computer == __paper__:
            print("You Win!!!")
        elif computer == __rock__:
            print("Computer Wins")
    else:
        print("Please enter a valid input(rock,paper or scissors)")

    
elif game_mode == 2:
    #play with each other
    start = input("Press any key to start the game")
    print("Enter Player 1 choice: ")
    player1 = input().lower()
    print("** NO CHEATING** \n " * 50)
    print("Enter Player 2 choice: ")
    player2 = input().lower()

    if player1 == player2:
        print("It's a draw")
    elif player1 == __rock__:
        if player2 == __scissors__:
            print("Player 1 Wins")
        elif player2 == __paper__:
            print("Player 2 Wins")
    elif player1 == __paper__:
        if player2 == __rock__:
            print("Player 1 Wins")
        elif player2 == __scissors__:
            print("Player 2 Wins")
    elif player1 == __scissors__:
        if player2 == __paper__:
            print("Player 1 Wins")
        elif player2 == __rock__:
            print("Player 2 Wins")
    else:
        print("Please enter a valid input(rock,paper or scissors)")
else:
    print("Please enter a valid game mode (1 or 2)")
