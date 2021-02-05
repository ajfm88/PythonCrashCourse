#three major rivers and the country each river runs through.
rivers = {
    'nile': 'egypt',
    'amazon': 'venezuela',
    'mississippi': 'usa',
}

#Use a loop to print a sentence about each river, such as The Nule runs through Egypt

for river, country in rivers.items():
    print(f"\nThe {river.title()} runs through {country.title()}.")

#Use a loop to print the name of each river

for river in rivers.keys():
    print(f"\n{river.title()}.")

#Use a loop to print the name of each country included in the dictionary.

for country in rivers.values():
    print(f"\n{country.title()}.")