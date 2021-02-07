favorite_numbers = {
    'kojima': [34, 55, 67],
    'miyamoto': [25, 98, 35],
    'molyneux': [14, 43, 72],
    'hamilton': [7, 12, 79],
    'dostoevsky': [10, 45, 63],
}

for name, favoritenumber in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in favoritenumber:
        print(number)