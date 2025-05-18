plateno = str(input("Enter the vehicle number to be validated: "))
plateno = plateno.replace('S', '', 1)

#Assigning numbers for the letters and assigning rest of the number to vars
char = plateno[0]
num1=int(ord(char.upper())-ord("A")+1)
char = plateno[1]
num2=int(ord(char.upper())-ord("A")+1)
num3 = int(plateno[2])
num4 = int(plateno[3])
num5 = int(plateno[4])
num6 = int(plateno[5])

#Using modulus to find where to reference from refstr
operation = ((num1*9)+(num2*4)+(num3*5)+(num4*3)+(num5*3)+(num6*2))%19
refstr = "AZYXUTSRPMLKJHGEDCB"
CorrLett = refstr[operation]

#Testing whether the letter is correct by referencing the last letter from the Car Plate
if CorrLett == plateno[-1]:
    print("Validity of the vehicle number: Valid")
else:
    print("Validity of the vehicle number: Invalid")