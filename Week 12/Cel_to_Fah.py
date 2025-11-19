c = float(input("Enter the temperature in degree Celsius: "))

def ctof():
    f = (c * 9 / 5) + 32
    return f

f = ctof()

print("The temperature is equivalent to {:1f} Fahrenheit.".format(f))