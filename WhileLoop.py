count=0
total=0
averge=0
while True:
    try:
        num = raw_input("> Enter a Number\n")
        if(num == "done"):
            break
        num = int(num)
        count = count + 1
        total = total + num
        
    except:
        print("OOPS ..! INVALID input\n")
print(" Count = {0}".format(count))
print(" Total = {0}".format(total))
print(" Average = {0}".format(total/count))
