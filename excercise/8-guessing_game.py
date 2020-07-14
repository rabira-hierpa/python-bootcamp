import random

random_number = random.randint(1,10)  # numbers 1 - 10
game_over = False
game_menu = "Guess a number between 1 and 10"
user_guess = input(game_menu)
while game_over is False:
    if int(user_guess) == random_number:
        print("You guessed it. You won!")
        replay = input("Do you want to play again? (y/n)")
        if replay == "y":
            game_over = False
        else:
            print("Thanks for playing. Bye!")
            game_over = True    
    elif int(user_guess) > random_number:
        print("Too high, try again!")
        user_guess =input(game_menu)
    else:
        print("Too low, try again!")
        user_guess = input(game_menu)
    
# handle user guesses
#   if they guess correct, tell them they won
#     otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!
