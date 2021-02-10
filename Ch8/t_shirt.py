#Write a function called make_shirt() that accepts a size and the text of a message
#that should be printed on the shirt. The fuction should print a sentence summarizing
#the size of the shirt and the message printed on it.
#Call the function once using positional arguments to make a shirt. 
#Call the function a second time using keyword arguments.

def make_shirt(size, text_of_a_message):
    """Displays information about the tshirt"""
    print(f"\nThe size of the t-shirt is {size}.")
    print(f"\nThe text on the t-shirt is {text_of_a_message}.")

make_shirt('5', 'Real Madrid')
make_shirt(size='7', text_of_a_message='Barcelona')