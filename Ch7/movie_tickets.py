#A movie theater charges diffferent ticket prices depending on a person's age.
#If a person is under the age of 3, the ticket is free;
#If they are between 3 and 12, the tiket is $10
#If they are over the age of 12, the ticket is $15.
#Write a loop in which you ask users their age, 
#and then tell them the cost of their movie ticket.

prompt = "Welcome to the movie theater. Please enter your age."
prompt += "and we will tell you the cost of your movie ticket (write 'quit' to end): "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    
    if age < 3:
        print(f"\n You are {age} years old. Your ticket is free.")
    elif age <= 12:
        print(f"\nYou are {age} years old. Your ticket is $10.00")
    elif age > 12:
        print(f"\nYou are {age} years old. Your ticket is $15.00")