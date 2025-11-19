def find_larger(n1, n2):
     if (n1 > n2):
          return n1
     else:
          return n2
     
#Can also use subtraction
n1 = int(input("Enter the first integer number: "))
n2 = int(input("Enter the second integer number: "))
n3 = int(input("Enter the third integer number: "))
n4 = int(input("Enter the fourth integer number: "))

larger1 = find_larger(n1, n2)
larger2 = find_larger(n3, n4)
largest = find_larger(larger1, larger2)
print('The largest integer is {}.'.format(largest))