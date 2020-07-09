choice = None
print('Choose your unit of mesurement')
print('\t 1.Kms')
print('\t 2.Mile')
choice = int(input('You choice:\t'))
if choice == 1 :
    user_input = input('How many kilometers did you run today?')
    kms = float(user_input)
    mile = round(kms/1.60934,2)
    print('You ran ' + str(mile) + ' miles today!')
else:
    user_input = input('How many Miles did you run today?')
    miles = float(user_input)
    kms = round(miles*1.60934,2)
    print('You ran ' + str(kms) + ' kms today!')
