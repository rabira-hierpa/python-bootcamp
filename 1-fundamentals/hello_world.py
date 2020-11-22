#  Python3 Fundamentals
#  This is a single line comment
print('Hello Python')  # prints an argument that is passed to it
print('Hello World')
print('Hellooooo')

x = 2    # int variable
print(type(x))  # returns the type of the var 'x' which is int
y = 1.2  # float var
print(type(y))  # returns the type of the var 'y' which is float
# Arithmatic Operations PEMDAS order
print(x + y)  # returns float (3.2)
print(x * y)  # multiplies two operands
print(x ** 8)  # raises x by power of 2
print(1 / 2)  # division ALWAYS RETURNS FLOAT!!!
print(1//2)  # integer division ALWAYS RETURNS INT
print(10 % 3)  # returns the remainder of the division

z = 'hello'
print(z ** x)  # muliplies and concatnates the string with non-int type
print(z * 2, end='\n')  # you can specifiy the end line character

__priavt_vars__ = 2
print(__priavt_vars__)  # ment to be constant i.e. not changed

# Data types
bols = True  # boolean must be True or False (capital letter)
print(bols)
game_over = False
print(game_over)
plyr_name = 'xyz'  # string var
print(plyr_name)
print(type(plyr_name))
plyr_name = 'TRUE'  # still string
print(plyr_name)

''' This is a multiline string
    NOT A MULTILINE COMMENT!!!
'''
# LIST - always starts with [square_brackts]
friuts = ['Banana', 'Apple', 'Orange', 'Pineapple']  # ordered sequ. of values
# DICTIONARY - always starts with {curly braces}
# key-value pair collection of objects
player = {'first_name': 'Rabra', 'last_name': 'Hierpa'}
print(friuts)
print(player)

# NONE a special data type  like null in JavaScript(python's version of null)
dob = None  # assume date of birth(dob) is not defined by a user
print(dob)  # prints None i.e similar to null in JS
person = {'name': 'Daisy', 'age': 30, 'child': None}
print(person.get('child'))  # reference a particular key using Get value
print(person['name'])  # alternative to person.get('name')
print(type(person.get('child')))  # None is a type of NoneType

# Declaring a string
# Single or double quotes doesn't matter but make sure you stay consistent
# in you file

my_str = 'my cat'
msg = 'he said "hello there!"'
print(msg)
# OR using single quotes inside double quotes
msg = "he said 'hello there!'"
print(msg)

# String Escape characters
new_line = 'hello\nworld'
print(new_line)
string = 'this is a backslash \\'
print(string)
# backspace escape character(deletes one character backwards)
message = 'pyth\bon'
print(message)

# String concatination
word2 = "face"
word1 = "book"
print(word2 + word1)
str_one = "ice"
str_one += " cream"  # useful when re assigning a string
print(str_one)
# Concatination only works with strings!!!
# Multiplication of strings
print('he' + 'l' * 2 + 'o' * 30)
print('Happy ' * 5 + 'Birthday!')
print('hello\vworld')
print('hello\fworld')
# String interpolation in python
# There are several ways to format strings
# The new way is to user F-String
x = 10
formatted = f'I\'ve told you {x*10 - 10} times already !'
print(formatted)
# x += 1
print(formatted)
# The tired-and true way python 2 -> 3.5
x = 10
print('I\'ve told you {} times already!'.format(x * x))
fruit = 'Banana'
ripeness = 'unripe'
print('The {} is {}'.format(fruit, ripeness))

# Converting Data Types
# In string interpolation, dataypes are implicitly
# converted into string form

# You can also explicitly convert variables by
# using the name of the built in types as a function
decimal = 14.12842423
integer = int(decimal)
comp = complex(decimal)
float_num = float(decimal)
print(integer, comp, float_num)
# Can also be done with long
simple_list = [43, 24, 23]
list_as_str = str(simple_list)
print(simple_list)
print(list_as_str + ' is printed as a string concatenated with this sentence')
print(str(8))

# Overrinding a reserved word wil result
# in error when you try to use the original word again!
int = "This is an integer"
print(int(9))  # TypeError : 'str' object is not callable
# Convert a string to lower case
print("DOCUMENT IMAGE RETRIEVAL WITH IMPROVEMENTS IN DATABASE QUALITY".lower())
# Convert a string to title case
print("Ha Nnu Kauniskangas".title())
