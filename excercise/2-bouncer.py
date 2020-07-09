 # ask for age
age = input('How old are you? ')

# alternative syntax is if age -> checks if age is not empty by default
if age != '' and int(age) > 0:
    age = int(age)
    if age >= 18 and age <= 21:
        print('You can enter, but need a wristband!')
    elif age >= 21:
        print('You are good to enter and can drink')
    else:
        print('You can\'t come in, littel one! :(')
else:
    print('Please enter a valid age')
