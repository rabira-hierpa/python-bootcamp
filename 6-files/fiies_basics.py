# Coursera Learning
# File handling basics
# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname, 'r')
    for line in fh:
        line = line.rstrip().upper()
        print(line)

except:
    print("Unable to read file! Please try again")
    quit()
