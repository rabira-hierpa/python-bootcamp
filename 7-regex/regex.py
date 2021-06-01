import re
x = 'My 2 favorite numbers are 18 and 22'
y = re.findall('[0-9]+',x)
print(y)
y = re.findall('[AEeIOU]+',x)
print(y)

x = 'From: Using the : character'
y = re.findall('^F.+?:',x)
print(y)