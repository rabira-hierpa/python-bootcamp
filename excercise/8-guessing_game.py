import random

random_number = random.randint(1,10)  # numbers 1 - 10
user_guess = None
while True:
    game_menu = input("Guess a number between 1 and 10 ")
    user_guess = int(game_menu)
    if user_guess:
        if int(user_guess) == random_number:
            print("You guessed it. You won!")
            replay = input("Do you want to play again? (y/n)")
            if replay.lower() == "y":
                user_guess = None
            else:
                print("Thanks for playing. Bye!")
                break  
        elif int(user_guess) > random_number:
            print("Too high, try again!")
        else:
            print("Too low, try again!")
    else:
        print("Please enter a valid value!!! ")
