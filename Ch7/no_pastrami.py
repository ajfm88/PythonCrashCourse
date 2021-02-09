sandwich_orders = ['tuna sandwich', 'pastrami sandwich', 'cuban sandwich']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made you a {current_sandwich.title()}!")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been made: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())