import random

def is_even(n):
    if (n % 2 == 0):
        return True
    else:
        return False
    
for i in range(5):
    number = random.randint(0, 100)
    if is_even(number):
        print('{} is even'.format(number))
    else:
        print('{} is odd.'.format(number))
