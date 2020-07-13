## In Python, for loops are written like this:
## for item in iterabel_object:
##      do something
## OR 
## for value in range(initalValue,endValue,stepValue):
##      do something
# for char in "hello":
#     print(char)

## For loops with ranges
number = 0
sums = 0

## the value of count is actually 4 since sequences start with 0
# for count in range(5):
#     number = eval(input("Enter an integer: "))
#     sums += number

# print("Sum is " + str(sums))
# print("Count is " + str(count))

# one parameter for loop
for var in range(7):
    print(var)

# two parameter for loop
for var in range(10,20):
    print(var)

# three pararmeter for loop
for x in range(1, 20, 2):
    print(x)
    # print(x*x)

for letter in "coffee":
    print(letter * 10)

r = range(20)
# list(r) can print in the python 3 RELP env
