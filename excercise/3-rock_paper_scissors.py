print("Welcome to the game!")
print("ROCK PAPER SCISSORS")
## constatns
__rock__ = "rock"
__paper__ = "paper"
__scissors__ = "scissors"

print("Please choose your game mode ")
print("\t Play with the computer")
print("\t Multiplayer ( 2 Players ) ")
game_mode = input()
game_mode = int(game_mode)
if game_mode == 1:
    #play with the computer
else:
    start = input("Press any key to start the game")
    print("Enter Player 1 choice: ")
    player1 = input()
    print("** NO CHEATING** \n " * 50)
    print("Enter Player 2 choice: ")
    player2 = input()

    if player1 == player2
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
