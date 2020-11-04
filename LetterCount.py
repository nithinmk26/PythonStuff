message = raw_input("Enter the word or message\n")
letter = raw_input("Enter letter to be count\n")

def countLetter(message,letter):
    total = 0
    for i in message:
        if(i == letter):
             total = total + 1
    return total

total = countLetter(message,letter)
print("TOTAL = %d" %total)


#word = 'banana'

#def cl(word):
#    count = 0
#    for letter in word:
#        if letter == 'a':
#            count = count + 1
#    print(count)
#cl(word)
