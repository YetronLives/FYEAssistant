width = int(input("Enter a width: "))
height = int(input("Enter a length: "))
symbol = input("Enter a symbol ")

for i in range(height):
    for j in range(width):
        print(symbol, end='')
    print()

