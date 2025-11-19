
char = input("Enter a character: ")
num = int(input("Enter a number: "))

for level in range(num):
    start_pos = num - level - 1

    #print the leading spaces
    for i in range(start_pos):
        print(' ', end="")

    #print the symbols
    for i in range(level + 1):
        print(char, end = ' ')

    print()

print("Merry Christmas!")