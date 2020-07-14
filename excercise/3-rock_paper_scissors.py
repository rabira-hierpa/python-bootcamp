from random import randint

print("Welcome to the game!")
print("ROCK PAPER SCISSORS")
## constatns
__rock__ = "rock"
__paper__ = "paper"
__scissors__ = "scissors"
computer_wins = 0
player_wins = 0
draws = 0
while True:
    print("Please choose your game mode ")
    print("\t 1. Play with the computer")
    print("\t 2. Multiplayer ( 2 Players ) ")
    print("\t 3. Quite Game ")

    game_mode = input("You're choice: \t")
    # play with the computer
    if game_mode == "1":
        #play with the computer
        print("*" *100)
        print("\t Enter quite or q to quite the game")
        print("*" * 100)
        while True:
            computer = ""
            rand_num = randint(0, 2)
            if rand_num == 0:
                computer = __rock__
            elif rand_num == 1:
                computer = __paper__
            else:
                computer == __scissors__
            player = input("Enter your move: ").lower()
            if player == "QUIT".lower() or player == "Q".lower():
                print("Thanks for playing the game. Bye !!!")
                break
            print("Computer move was " + computer.upper())
            print("Your move was " + player.upper())
            if player == computer:
                print("It's a draw")
                draws += 1
            elif player == __rock__:
                if computer == __scissors__:
                    print("You Win!!!")
                    player_wins+=1
                elif computer == __paper__:
                    print("Computer Wins")
                    computer_wins +=1
            elif player == __paper__:
                if computer == __rock__:
                    print("You Win!!!")
                    player_wins += 1
                elif computer == __scissors__:
                    print("Computer Wins")
                    computer_wins +=1
            elif player == __scissors__:
                if computer == __paper__:
                    print("You Win!!!")
                    player_wins += 1
                elif computer == __rock__:
                    print("Computer Wins")
                    computer_wins +=1
            else:
                print("Please enter a valid input(rock,paper or scissors)")
            print("PLAYER wins " + str(player_wins) + " COPMUTER Wins " + str(computer_wins) + " DRAWS: " + str(draws))
    #play with each other
    elif game_mode == "2":
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
    # quite the
    elif game_mode == "3":
        print("Quitting game...")
        break
    else:
        print("Please enter a valid game mode (1, 2 or 3)")
