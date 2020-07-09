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

    if player1 and player2:
        if (player1 == __rock__ and player2 == __paper__):
            print("Player 2 wins")
        elif (player2 == __rock__ and player1 == __paper__):
            print("Player 1 wins")
        elif (player1 == __rock__ and player2 == __scissors__):
            print("Player 1 wins")
        elif (player2 == __rock__ and player1 == __scissors__):
            print("Player 2 wins")
        elif (player1 == __paper__ and player2 == __scissors__):
            print("Player 2 Wins")
        elif(player1 == __scissors__ and player2 == __paper__):
            print("Player 2 wins")
        elif player1 == player2:
            print("DRAW!!!")
    else:
        print("Please enter a valid input(rock,paper or scissors)")
