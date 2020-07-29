# Lists are fundamental data structures for orginizing data
# they are similar to arrays in java and cpp
# Syntax
# var = [item1,item2,item3,...,item4] --> using squre brackets
# list() --> using the built-in function
# the first index of a list is always zero same as range()
demo_list = ['strings', 1, 2, True, False, 7.4]
print(demo_list)
# how many elemnts exists with a list - we can use len
print("Length of demo_list ", len(demo_list))
# you can convert a range into a list
rng = range(1, 20)
print(rng)  # prints range(1,20)
print(list(rng))  # prints [1,2,3,4,...,20]

# Simple example to print a list
# notice that we DON'T USE len() to figure
# out the lenght of the list as we do with
# arrays in other programming languages

# similar to forEach loop in JavaScript
for element in demo_list:
    if type(element) == str:  # checks if the element is type of string or not
        print("Type of element is string")
    print(element)  # prints each element in a single line


# print a single elment of a list
# with the index of the element in the list
print(demo_list[0])  # pritns "strings"
print(demo_list[3])  # pritns "True"


# Accessing values from the end
# Note that when accessing from
# the end the index value starts from -1 !!!
print(demo_list[-2])  # prints False
print(demo_list[-5])  # prints "strings"
# print(demo_list[-7])  # list index out of range error

# Check if a value is in alist
# you can use the keyword in

if "strings" in demo_list:
    print("The strings are a list !!!")


# Print using while loop
sample_list = [134, 241.4, 24, "LIST", "abc", True, False]
i = 0
while i < len(sample_list):
    print(f"item {i+1}: {sample_list[i]}")
    i += 1
    if 2 in sample_list:
        print("You're lucky")

# append method for a list
nums = [1, 2, 3]
nums.append([4, 5])
print(nums[3][0])  # prints 4
print(nums[3][1])  # prints 5
# extend method for linst
nums.extend([4, 5, 6, 7, 8, 9])
print(nums)
# insert method
nums.insert(2, 48)  # nums is now [1,2,48,3,4,5,6,7,8,9]
nums.insert(-2, 99)  # inserts 99 in place of 8
print(nums)  # nums [1,2,48,3,4,5,6,7,99, 8,9]
# to insert at the very last using insert method
nums.insert(len(nums), 14)
print(nums)

# clear a list
nums.clear()
print(nums)  # []
items = ["stock imgae", "mugs", "shoes", "t-shirts", "pants", "trainers"]
print(items)

items.pop()  # removes "trainers"
last_item = items.pop(4)  # removes "pants"
print(items)
print("Last item is " + last_item)
first_item = items.pop(0)
print(items)
print(first_item)

# remove method of a list
names = ["bitu", "deju", "edu", "mistere",
         "saron", "mesale", "mekdi", "Nazrawian"]
names.append("abi")
print(names)
names.remove("Nazrawian")
print(names)
names.insert(4, "Naz")
print(names)
names.append("Naz")
print(names)
names.remove("Naz")  # removes the 4th index naz not the last one!

# index method
names.index('bitu')  # prints 0
names.append("Naz")
names.insert(6, "Naz")
# ['bitu', 'deju', 'edu', 'mistere', 'saron', 'mesale', 'mekdi', 'Nazrawian']
print(names)

names.index("Naz")  # prints 6 since it is the first occurance
names.index("Naz", 7)  # prints 9 because the start position is the 7th index
# error Naz is not is the list becuase start and end index values are not inclusive
# names.index("Naz", 0, 6)
# coutn mehtod
names.count("Naz")  # prints 2

# reverse method
names.reverse()
print(names)  # reversed list

# sort
names.sort()
print(names)
names.append("Abi")

# note that you must surround your items to
# supply to the methoda as a single argument
names.extend(("Yoni", "abeni", "semera"))
print(names)
names.sort()
print(names)

# Find duplicates and remove them
for name in names:
    if names.count(name) > 1:
        names.remove(name)
print("New list of names is ", names)

names = names[2:7]  # contains only the first 6 names
firends = ", ".join(names)
print("Naz family includes " + firends)

# Slicing lists
second_list = list([1, 3, 4, 5, 7, 9, 11])
print(second_list[-1:])  # prints [11]
print(second_list[0:-1])  # prints [1,3,4,5,7,9]
print(second_list[-4:-2])  # prints [5,7]
print(second_list[-2:0])  # prints empty list - python doesn't wrap up
print(second_list[::2])  # steps by two - prints 1,4,7,11
# steps by w from the -2 index position which prints only 9
print(second_list[-2::2])
# starts from 0 increments by 3 and ends on the second index
print(second_list[:6:2])  # starts from 0 ends at 6 index and increment by 2
print(second_list[-1:0:-3])

friends = names
print(names)
print("I am friends with: ".join(friends) + "\n")
print("  is my friend. ".join(friends))

# Reversing a list
friends[::-1]  # is in place (doesn't create a new list)
print(friends)
friends = friends[::-1]
print(friends)
mis = friends[2][::-1]  # reverses each character of a given name
print(mis)
print("rabra hierpa"[::-1])

# Swapping values
store = list(["desk", "chair"])
print(store)
print(names)
names[0], names[1] = names[1], names[0]
print("After swapping values (index 0 and 1)")
print(names)
