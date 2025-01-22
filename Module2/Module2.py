# IF/ELSE STATEMENTS
#EX 1
if True:
    print("Yes") # This statement will  print out "Yes"
else:
    print("No")  # This statement will not print

# OUTPUT: Yes

#EX 2
x = 5
if x > 10:
    print("A") # This will not print as 5 is not greater than 10
elif x > 4:
    print("B") # This will print as 5 is  greater than 4
elif x > 2:
    print("C") # Though 5 is also greater than 2, because this is an else if(elif) setup,
               # Only the first true statement evaluates, everything else is ignored.
else:
    print("D") # Does not print out

# OUTPUT: B

#EX 3
x = 5
if x > 10:
    print("A") # This will not print as 5 is not greater than 10
if x > 4:
    print("B") # This will print as 5 is  greater than 4
if x > 2:
    print("C") # Because this is an if, it evaluates as though nothing is
               # before it, hence evaluating to true as 5 is greater than 2
               # and prints out "C"
else:
    print("D") # since this else is connected to the previous if, it will
               # not print out D since the if statement was true.

# OUTPUT: B
#         C


#MATCH CASE