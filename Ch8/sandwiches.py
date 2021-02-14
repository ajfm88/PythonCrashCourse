#Write a function that accepts a list of items a person wants
#on a sandwich. The function should have one parameter that collects as many
#items as the function call provides, and it should print a summary of the sand-
#wich that’s being ordered. Call the function three times, using a different num-
#ber of arguments each time.

def make_sandwiches(*toppings):
    """Print the list of toppings that have been requested"""
    print(toppings)

make_sandwiches('ham')
make_sandwiches('cheese', 'ham', 'bacon', 'tomato', 'lettuce')