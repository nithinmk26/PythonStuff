fname = raw_input("Enter the file name \n")
wordList = []

def openFileAndSplit(fname):
    count = 0
    try:
        fhand = open(fname+".txt")
        for line in fhand:
            for word in line.split():
                if(word in wordList):
                    count = count + 1
                    continue
                else:
                    wordList.append(word)
                    
    except:
        print("File Doesnt Exists..!\n")
    return count


totalRepetative = openFileAndSplit(fname)
print(" Total Repetatives are : ",totalRepetative)
wordList.sort()
print(wordList)
