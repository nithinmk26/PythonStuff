print("Welcome to Nanda's Pay System\n")

hoursWorked = float(raw_input("Enter The Hours Worked..!\n"))
rate = int(raw_input("Enter the Rate per Hour...!!\n"))

def computepay(hoursWorked,rate):
    if(hoursWorked <= 40):
        print ("Payable Amount is " , hoursWorked*rate)
    elif(hoursWorked >40):
        payFor40 = 40 * rate
        hoursTotal = payFor40 +( ((hoursWorked - 40) * 1.5) * 10)
        print ("Payable Amount is " ,hoursTotal)


computepay(hoursWorked,rate)
    
