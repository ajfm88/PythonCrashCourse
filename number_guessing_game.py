from random import randint

target = randint(1,100)
counter = 1

while True:
    while True:
        guess = input("Please enter a number: ")
        if guess.isdecimal():
            guess = int(guess)
            break
        else:
            print("Please enter a valid number between 1-100")

    if guess > target:
        print("Your guess is too high.")
    elif guess < target:
        print("Your guess is too low.")
    else:
        print("Congratulations!")
        break
    counter += 1

print(f"End of execution! Number of guesses: {counter}")