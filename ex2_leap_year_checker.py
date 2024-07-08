daysinyear = int(input("Enter your year"))
if daysinyear%400==0:
    print ("This is a leap year")
elif daysinyear%4==0 and daysinyear%100!=0:
    print("This is a leap year")
elif daysinyear%400!=0:
    print("This is NOT a leap year")
elif daysinyear%4!=0 or not daysinyear%100==:
    print