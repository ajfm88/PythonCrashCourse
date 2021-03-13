#Write a program that prompts for the user’s favorite
#number. Use json.dump() to store this number in a file. Write a separate pro-
#gram that reads in this value and prints the message, “I know your favorite
#number! It’s _____.”

import json

number = input("What's your favorite number? ")

with open('favorite_number.json', 'w') as f:
    json.dump(number, f)
    print("Thanks! I'll remember that.")