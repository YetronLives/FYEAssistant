def Add(n, m):
    return n + m

def Subtract(n, m):
    return n - m

def Multiply(n, m):
    return n * m

def Divide(n, m):
    return n / m

def Remainder(n, m):
    return n % m

def Most(n, m):
    if n > m:
        return n
    return m
        
def Least(n, m):
    if n > m:
        return m
    return n
        
while True:
    print('''        
1. Add
2. Subtract
3. Multiply
4. Divide
5. Remainder
6. Most
7. Least
8. Quit''')
    choice = int(input("What would you like to do: "))

    if choice == 8:
        print("Quitting program...")
        break

    if 1 > choice > 7:
        continue

    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    

    match choice:
        case 1:
            print(f"The sum is {Add(n1, n2)}")
        case 2:
            print(f"The diffrence is {Subtract(n1, n2)}")
        case 3:
            print(f"The product is {Multiply(n1, n2)}")
        case 4:
            print(f"The quotent is {Divide(n1, n2)}")
        case 5:
            print(f"The remainder is {Remainder(n1, n2)}")
        case 6:
            print(f"The greates number is {Most(n1, n2)}")
        case 7:
            print(f"The least number is {Least(n1, n2)}")
