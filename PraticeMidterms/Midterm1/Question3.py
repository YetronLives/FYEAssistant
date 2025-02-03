def game():
    correct = 0

    q1 = input("Please enter question 1: ")
    q1a = input("Please enter the anwser to question 1: ")
    q2 = input("Please enter question 2: ")
    q2a = input("Please enter the anwser to question 2: ")
    q3 = input("Please enter question 3: ")
    q3a = input("Please enter the anwser to question 3: ")

    anwser1 = input(f"{q1}: ")
    anwser2 = input(f"{q2}: ")
    anwser3 = input(f"{q3}: ")

    if anwser1 == q1a:
        correct+=1
    if anwser2 == q2a:
        correct+=1
    if anwser3 == q3a:
        correct+=1

    print(f"You got {correct} out of 3 correct")


game()
