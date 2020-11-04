print("FIZZ BUZZ Problem in python\n")


lastNum = raw_input("Enter the last Number\n")

try:
    lastNum = int(lastNum)
    for i in range(1,lastNum+1):
        if(i%3 == 0 and i%5==0):
            print("FIZZ BUZZ")
        elif(i%3==0):
            print("FIZZ")
        elif(i%5==0):
            print("BUZZ")
        else:
            print(i)

except:
    print("Enter the Valid Number..!")

raw_input("Press Enter to exit..")
