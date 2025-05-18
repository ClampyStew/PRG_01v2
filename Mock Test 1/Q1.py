wantedLoan = float(input("What is your desired loan amount? "))
annSalary = float(input("What is your annual income? "))
currLoan = float(input("What is the total value of your current loans? "))
totalSaving = float(input("What is the total of your savings? "))
intendYears = float(input("How many years do you want to pay back this loan? "))

totalLoan = ((wantedLoan+currLoan)/(totalSaving+(annSalary*intendYears)))
loanpercent = float(totalLoan * 100)

print(f"{"Your interest rate is "}{loanpercent:.1f}{"%"}")