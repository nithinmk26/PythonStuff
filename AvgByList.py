numList = []
while True:
    num = raw_input("Entr the NUmber \n")
    try:
        if(num == 'done'):
            break
        num = int(num)
        numList.append(num)
    except:
        print("ENter the Number as an input\n")

print("Total - ", sum(numList))
print("Count - ", len(numList))
print("Average - ", sum(numList)/len(numList))
