
def makePattern(n):

    layers = n // 2

    #this determins the amount of layers before and after the base layer we will have to print
    #
    #   *
    #  ***
    # ***** <--- This is the base layer
    #  *** 
    #   *
    #
    # so if n is 5, we will have to print two layers above and below the base layer


    # This prints the top layer
    for i in range(layers):
        # in each itteration we print layers - i spaces
        print(" " * (layers - i), end="")
        # we then print ((2 * i) + 1) stars
        print("*" * ((2 * i) + 1), end="")
        # the print is here to make a new line
        print()

    # This prints the base layer, we dont need to do any math to figure out
    # how many stars we have to print herek, because it is just n stars
    print("*"*n)

    # This prints the bottom layer
    for i in range(layers):
        # we print (i + 1) spaces
        print(" " * (i + 1), end="")
        # we then print (n - ((i + 1) * 2)) stars 
        print("*" * ((n) - ((i + 1) * 2)), end="")
        # the print is here to make a new line
        print()

# This while loop repeats untill the user inputs an odd number
while True:
    userInput = int(input("Please enter an odd number: "))
    if userInput % 2 == 1:
        break

# We call our function
makePattern(userInput)




