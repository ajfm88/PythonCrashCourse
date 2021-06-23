from random import randint

ROCK = 1
PAPER = 2
SCISSORS = 3

while True:
    while True:
        print("Welcome to Rock, Paper, Scissors!")
        print("Please choose which move to make: ")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        userInput = input(">: ")
        if userInput.isdecimal():
            userInput = int(userInput)
            if 1 <= userInput <= 3:
                break
            else:
                print("Please enter a number between 1 and 3.")
        else:
            print("Please enter a valid number.")

    compChoice = randint(1,3)

    print(f"Player: {userInput}, Computer: {compChoice}")

    if userInput == ROCK:
        if compChoice == SCISSORS:
            print("Player won!")
        elif compChoice == PAPER:
            print("Computer won!")
        else:
            print("Draw!")

    if userInput == PAPER:
        if compChoice == ROCK:
            print("Player won!")
        elif compChoice == SCISSORS:
            print("Computer won!")
        else:
            print("Draw!")

    if userInput == SCISSORS:
        if compChoice == PAPER:
            print("Player won!")
        elif compChoice == ROCK:
            print("Computer won!")
        else:
            print("Draw!")