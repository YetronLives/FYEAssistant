# Prompts the user to enter their name, then saves it to a variable called name
name = input("Please enter your name: ")

#Prompts the user to enter their age, then saves it to a variable called name
age = int(input("Please enter your age: "))

# Prompts the user to enter their name, then saves it to a variable called name
favoriteFood = input("Please enter your favorite food: ")

# Printing the string Your xxx is:, then printing the variable name that holds the corresponding input
print("Your name is:", name)
print("Your age is:", age)
print("Your favorite food is:", favoriteFood)


'''
In this example it is fine to not cast the age input as an integer because we are just printing it, 
but if later we wanted to do math with their age we would have to convert it to a number,
I did it anyways as it is good pratice.
'''
