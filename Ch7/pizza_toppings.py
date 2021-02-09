prompt = "\nPlease enter your favorite pizza toppings: "
prompt += "\nEnter 'quit' to end the program."

message = ""
while message != 'quit':
    message = input(prompt)
    print(f"You have added {message} to your pizza!")