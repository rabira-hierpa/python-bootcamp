# Execercise form w3resources
# Link => https://www.w3resource.com/python-exercises/list/

from random import randint
lists = []
for i in range(1, 15):
    num = randint(1, 100)
    lists.append(num)

# 1. Write a Python program to sum all the items in a list
print(lists)
print("Sum of list is " + str(sum(lists)))
# 2. Write a Python program to multiplies all the items in a list.
newlist = []
count = 0
for i in lists:
    newlist.append(i * 2)
    count += 1
    print(f'{count}' + str(newlist))

# 3. Write a Python program to get the largest number from a list.
print("Max num is " + str(max(lists)))

# 4. Write a Python program to get the smallest number from a list.

print("Min num is " + str(min(lists)))

# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

string_list = ["tat", "ini", "door", "ad", "rand",
               "rar", "mom", "1991", "2002", "2020", "dad", "4333"]

print("The current list is ")
print(string_list)

total = 0
for string in string_list:
    if len(string) > 2 and string[0] == string[-1]:
        total += 1

print(f"Total words found {total}")

# 6. Remove duplicates within a list!
for
