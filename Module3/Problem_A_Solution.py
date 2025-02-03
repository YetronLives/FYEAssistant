
def area(l,w):
    shape = input("Do you want to calculate the area of the square or triangle: ")
    match shape:
        case "square":
            return l * w
        case "triangle":
            return .5*(l*w)

length = int(input("Enter length: "))
width = int(input("Enter width: "))

print(f"The area is {area(length, width)}")
