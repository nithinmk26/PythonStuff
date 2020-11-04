fhand = open('C:/Users/M1056182/Desktop/Python/nanda.txt','r')
count = 0
for line in fhand:
    if(line.startswith("It")):
       print(line)
    if(line.find("Lorem")):
        for i in line.split():
            print (i.upper())
    count = count + 1
print("Count - {0}".format(count))
