import random
num1 = random.randint(0,100)
num2 = random.randint(0,100)

userAnswer = int(input("Enter the sum of {} and {}:".format(num1,num2)))
correctAnswer =num1+num2

if userAnswer == correctAnswer:
    print("Your answer is correct!")
else:
    print("Your answer is wrong. \nThe correct answer is {}.".format(correctAnswer))