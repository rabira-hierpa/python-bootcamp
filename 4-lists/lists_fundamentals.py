# Lists are fundamental data structures for orginizing data
# Syntax
# var = [item1,item2,item3,...,item4] --> using squre brackets
# list() --> using the built-in function
# the first index of a list is always zero same as range()
demo_list = ['strings', 1, 2, True, False, 7.4]
print(demo_list)
# how many elemnts exists with a list - we can use len
print("Length of demo_list " + str(len(demo_list)))
# you can convert a range into a list
rng = range(1, 20)
print(rng)  # prints range(1,20)
print(list(rng))  # prints [1,2,3,4,...,20]

# Simple example to print a list
# notice that we don't use len() to figure
# out the lenght of the list as we do with
# arrays in other programming languages

# similar to forEach loop in JavaScript
for element in demo_list:
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
nums.append([4,5])
print(nums[3][0]) # prints 4
print(nums[3][1]) # prints 5
# extend method for linst
nums.extend([4, 5, 6, 7, 8, 9])
print(nums)
# insert method 
nums.insert(2,48) # nums is now [1,2,48,3,4,5,6,7,8,9]
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
items.pop() # removes "trainers"
last_item = items.pop(4) # removes "pants"
print(items)
print("Last item is " + last_item)

