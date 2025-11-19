def print_character(char, n):
    for i in range(n):
        print(char, end='')
    print()

def print_square(size, char):
    for i in range(size):
        print_character(char, size)

char = input("Enter the character: ")
side = int(input("Enter the side of the square: "))
print_square(side, char)