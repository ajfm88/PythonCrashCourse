from random import randint

target = randint(1,100)
counter = 1

while True:
    while True:
        guess = input("Please enter a number between 1 and 100: ")
        if guess.isdecimal():
            guess = int(guess)
            break
        else:
            print("Invalid input. Please enter a valid number between 1 and 100.")
    if guess > target and counter < 10:
        print(f"Your guess is too high. Please try again. You have used {counter} out of 10 tries.")
        counter = counter + 1
    elif guess < target and counter < 10:
        print(f"Your guess is too low. Please try again. You have used {counter} out of 10 tries.")
        counter += 1
    elif guess != target and counter == 10:
        print(f"Game Over. You already used up your {counter} tries.")
        break
    elif guess == target:
        print(f"Congratulations, you have won the game! Tries used to complete the game: {counter}")
        break