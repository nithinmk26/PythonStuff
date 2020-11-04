print("Grading system against marks obtained...!")


score = raw_input("Enter the Score u obtained..!\n")
try:
    score = int(score)
    if(score > 100 or score < 0 ):
        print ("Enter a valid score between 0 to 100")
    elif(score > 0 and score <= 60):
        print("You Obtained  Grade  F")
    elif(score > 60 and score <= 70):
        print("You Obtained  Grade  D")
    elif(score > 70 and score <= 80):
        print("You Obtained  Grade  C")
    elif(score > 80 and score <= 90):
        print("You Obtained  Grade  B")
    elif(score > 90 and score <= 100):
        print("You Obtained  Grade  A")
except:
    print("Please Enter a valid Number as Input")
