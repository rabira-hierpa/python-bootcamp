# for i in range(1, 11):
#     print("\U0001f603" * i)

# num = 11
# while num > 1:
#     print("\U0001f603" * num)
#     num -= 1

# for num in range(1, 11):
#     count = 1
#     smilyes = ""
#     while count < num:
#         smilyes += "\U0001f603"
#         count += 1
#     print(smilyes)

# Centered pyramid(Simply triangle)
num = 1
space = 20
while num < 20:
    space -= 2
    print(str(" " * int(space //2)) + ("\U0001f603" * num) + str(" " * int(space//2)))
    num += 2
