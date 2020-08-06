# NUMBER_OF_ELEMENTS = 5
# num = []  # creates an empty list
# sums = 0
# count = 0
# print("Program to calcute an average and print numbers less than the average! 😕")
# for i in range(NUMBER_OF_ELEMENTS):
#     value = eval(input("Enter a number: "))
#     num.append(value)
#     sums += value

# average = sums / NUMBER_OF_ELEMENTS

# print("Numbers less than average")
# for i in range(NUMBER_OF_ELEMENTS):
#     if num[i] < average:
#         print(f"{num[i]} is less than the average {average}")
#         count += 1

# print("Average is ", average)
# print("Numbers less than average are ", count)

# List comprehension
nums = [1, 4, 5, 2, 8]
sqr_nums = []
# In for loop
for num in nums:
    sqr_nums.append(num * num)
print("Using for loop")
print(sqr_nums)
# using list comprehension
print("Using list comprehension")
print([x*2 for x in nums])

# Another example
names = ['edu', 'abigu', 'mistere', 'saron', 'deju',
         'fiker', 'mike', 'bezi', 'medki', 'aman', 'beste']

[name[0].upper() + name[1::] for name in names]

colors = ['red', 'oragen', 'violate', 'purple', 'pink', 'blue']

[color[0].upper() for color in colors]

nested_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nested_names = [['edu', 'Alex'], ['abigu', 'alex'], [
    'saron', 'addisu'], ['deju', 'tesfaye'], ['mekdi', 'terefe']]

[full_name[0].capitalize() for full_name in nested_names]

[num*num for num in range(1, 10)]

string_nums = ['24', '435', '21', '45', '87']

[int(num) + 1 for num in string_nums]

[num + 1 for num in string_nums]

# Nested lists
cords = [[10.45, 45.25], [42.14, 23.1], [32.34, 9.04]]
# Accessing nested lists
for loc in cords:
    print(loc)
    for lat_lan in loc:
        print(lat_lan)

# Same as the above nested loop
[[print(cord) for cord in loc] for loc in cords]


# Sample gameboard for a tic-tac-toe game
board = [[num for num in range(1, 4)] for val in range(1, 4)]

print(board)

[["X" if num % 3 != 0 else "O" for num in range(1, 4)] for num in range(1, 4)]

# Simple grid  3x3 with '*' character

[['*' for y in range(1, 4)] for x in range(1, 4)]
