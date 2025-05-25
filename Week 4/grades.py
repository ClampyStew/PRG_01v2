usermarks = float(input("Please enter your marks: "))

if usermarks >= 85:
    grade = "A+"
    comments = "Excellent!"
elif (usermarks >= 80) and (usermarks < 85):
    grade = "A"
    comments = "Well done"
elif (usermarks >= 75) and (usermarks < 80):
    grade = "B+"
    comments = ""
elif (usermarks >=70) and (usermarks < 75):
    grade = "B"
    comments = ""
elif (usermarks >= 65) and (usermarks < 70):
    grade = "C+"
    comments = ""
elif (usermarks >= 60) and (usermarks < 65):
    grade = "C"
    comments = ""
elif (usermarks >= 55) and (usermarks < 60):
    grade = "D+"
    comments = ""
elif (usermarks >= 50) and (usermarks < 55):
    grade = "D"
    comments = ""
elif (usermarks < 50):
    grade = "F"
    comments = "See me."

print("Grade: {}\n{}".format(grade, comments))
    