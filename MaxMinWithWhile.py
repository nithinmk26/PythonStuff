lowest = 1
greatest = 1
while True:
    try:
        num = raw_input("Enter a Num\n")
        if(num=='done'):
            break
        num = int(num)
        if(num<lowest):
            lowest=num
        elif(num>greatest):
            greatest=num
    except:
        print("ENter a valid Number..!")
print("HIGHEST NUMBER = {0}".format(greatest))
print("LOWEST NUMBER = {0}".format(lowest))
