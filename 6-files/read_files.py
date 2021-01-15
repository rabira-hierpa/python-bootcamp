# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
    count = 0
    total = 0.0
    average = 0.0
    for line in fh:
        line = line.rstrip()
        if not line.startswith("X-DSPAM-Confidence:"):
            continue
        number = line.split()[1]
        count = count + 1
        total = total + float(number)
    average = total / count
    average
    print("Average sapm confidence:", average, end='')
except:
    print("Unable to read file!Please try again")
    quit()
