#Make a list containing a series of short text messages. Pass the
#list to a function called show_messages(), which prints each text message.

def show_messages(messages):
    """Print a message inside a list."""
    for message in messages:
        msg = f"This is the message: {message}"
        print(msg)

messages = ['this is message 1', 'this is message 2', 'and this is message 3']
show_messages(messages)