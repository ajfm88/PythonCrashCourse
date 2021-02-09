#Make a list called sandwich_orders and fill it with the names of various sandwiches.

sandwich_orders = ['tuna sandwich', 'pastrami sandwich', 'cuban sandwich']
#Then make an empty list called finished_sandwiches.
finished_sandwiches = []
#Loop through the list of sandwich orders
#and print a message for each order, such as "I made your tuna sandwich."
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made you a {current_sandwich.title()}!")
    
#As each sandwich is made, move it to the list of finished sandwiches. 
    finished_sandwiches.append(current_sandwich)
# After all the sandwiches have been made, print a message listing each sandwich that was made.
print("\nThe following sandwiches have been made: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())