buffet_foods = ('fried_rice', 'orange_chicken', 'egg_roll', 'sushi', 'beef_and_broccoli')

print("You can choose from the following menu items:")
for foods in buffet_foods:
    print(f"- {foods}")

print("\nOur menu has changed.")
print("You can now choose from the following items:")
buffet_foods = ('fried_rice', 'orange_chicken', 'egg_roll', 'shrimp', 'dim_sun')
for foods in buffet_foods:
    print(f"- {foods}")