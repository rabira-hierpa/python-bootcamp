## Conditional logic in python follows almost the same
# common patterns in C,C++, Java and JavaScript and Bash/Shell
user_number = input('Guess a number')
user_number = int(user_number)
if user_number < 10:
    print('Number is less than 10')
elif user_number < 50:
    print('Your guess is less than 50')
elif user_number > 100:
    print('Your guess is greater than 100')
else:
    print('I don\'t know your number!')

cont = input('Do you want to contintue (y/N)')
if cont == 'y' or 'Y':
	usr_name = input('Guess a color ')
	if usr_name == 'uncommon red-pink combo':
		print('Your color tast is a weired one!')
	else:
		print('You have a normal color test!')

## Comparision ops in python are
# == equal to
# != not equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to

## Logical ops in python are
# and 
# or
# not
