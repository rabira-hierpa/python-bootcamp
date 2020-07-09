## New Turthiness expression in python3
x = 14
if x is 14:
	print('The nubmer x is ' + str(x))
elif x is not 14:
	print('The number x is not 14')
obj = object()
if obj:
    print('object() by default is True(Not Empty!)') # this ones gets printed!
else:
    print('object() by default is false!') 
if obj is {}:
    print('object() by default is True(Not Empty!)')
else:
    print('object() by default is false!') # this ones gets printed!
empyt_str = str()
if empyt_str:
    print('str() by default is True!')
else:
    print('str() by default is False!!!')

## In python '==' and 'is' are very similar 
# but they are not the same
list_a = [1,2,3]
list_b = [1,2,3]
if list_a == list_b:
    print('both list_a and list_b are the same') #this gets printed
else:
    print('both list_a and list_b are NOT the same')

# The same logic doesn't work with the 'is' operator
if list_a is list_b:
    print('both list_a and list_b are the same')
else:
    print('both list_a and list_b are NOT the same') #this gets printed
