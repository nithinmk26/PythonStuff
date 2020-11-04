faranhiet = raw_input("Enter Temp in Farenhiet \n")

try:
    faranhiet = float(faranhiet)
    celcius = (faranhiet - 32.0) * 5.0 / 9.0
    print("{0} faranhiet is equal to {1} Celcius".format(faranhiet,celcius))
except:
    print("Please Enter a Number")


raw_input("Press Enter To EXIT")
