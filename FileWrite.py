fname = raw_input("Enter File Name:  \n")

try:
    fhand = open(fname+".txt",'a')
    line = raw_input("Enter the message \n")
    fhand.write('\n')
    fhand.write(line)
except:
    print("File is not present to write..!")
finally:
    fhand.close()
