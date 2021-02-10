#Modify the make_shirt() function so that shirts are large by default
#with a message that reads I love Python.

def make_shirt(size='large', text_of_a_message='I love Python'):
    """Displays information about the tshirt"""
    print(f"\nThe size of the t-shirt is {size}.")
    print(f"\nThe text on the t-shirt is {text_of_a_message}.")

#Make a large shirt and a medium shirt with the default message, and a shirt of any size
#with a different message.

make_shirt()
make_shirt(size='medium')
make_shirt(size='small', text_of_a_message='I love HTML')