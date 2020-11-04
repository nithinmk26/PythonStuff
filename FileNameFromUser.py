fname = raw_input("Enter the file name\n")
try:
    fhand = open (fname+".txt")
    for line in fhand:
        print(line)
except:
    print("File is Not Present\n")
