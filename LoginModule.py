name = raw_input("Enter the user Name : \n")
password = raw_input("Enter the Password : \n")

#if(name=='Nanda' and password=="Nithin"):
   # print("Login SuccessFull...!")
if(name=='Nanda'):
    if(password=='Nithin'):
       print("Login SuccessFull...!")
elif(name=="Nanda"):
    print("Wrong Password..!")
elif(password=="Nithin"):
    print("Wrong User Name..!")
else:
    print("Please Re type user name and password....!")

raw_input(" Press Enter to EXIT...")
