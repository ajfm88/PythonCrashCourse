#Start with a copy of your program from Exercise 8-9.
#Write a function called send_messages() that prints each text message and
#moves each message to a new list called sent_messages as it’s printed. After
#calling the function, print both of your lists to make sure the messages were
#moved correctly.

def send_messages(unsent_messages, sent_messages):
    """prints each message"""
    while unsent_messages:
        current_message = unsent_messages.pop()
        print(f"Printing the message: {current_message}")
        sent_messages.append(current_message)

unsent_messages = ['this is message 1', 'this is message 2', 'and this is message 3']
sent_messages = []

send_messages(unsent_messages, sent_messages)

print("\nFinal lists:")
print(unsent_messages)
print(sent_messages)