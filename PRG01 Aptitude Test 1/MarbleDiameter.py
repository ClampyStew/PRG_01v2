#For Q1
import math

CupDiameter = float(input("Enter the diameter of the cup: "))
IniWaterH = float(input("Enter the initial water height: "))
FinWaterH = float(input("Enter the final water height: "))

#Calculating volume diff
WaterDiff = float(math.pi*((CupDiameter/2)**2)*FinWaterH)-(math.pi*((CupDiameter/2)**2)*IniWaterH)

MarbleBlue = (2*((3*WaterDiff)/(4*math.pi))**(1/3))
MarbleBlue = round(MarbleBlue, 2)

print("New marble's diameter is {}".format(MarbleBlue))