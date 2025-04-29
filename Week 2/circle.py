#This code aims to calculate the longest side of a right-angled triangle in the circle given 2 values in the triangle and also to calculate area of circle
import math

length = float(input('Enter the length of a: '))
base = float(input('Enter the length of b: '))

c = ((base**2)+(length**2))**(0.5)
radius = float(c/2)
area = float((math.pi)*(radius**2))

print ("The diameter of the circle is",c,'''
The area of circle is''', area )