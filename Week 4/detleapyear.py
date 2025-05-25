yearinq = int(input("Please enter the year: "))



if ((yearinq % 4) == 0) and ((yearinq % 100) > 0):
    leapYear = "a leap year."
elif ((yearinq % 400) == 0):
    leapYear = "a leap year."
else: 
    leapYear = "not a leap year."


print("{} is {}".format(yearinq, leapYear))