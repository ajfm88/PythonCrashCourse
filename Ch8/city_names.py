#Write a function called city_country() that takes in the name of a city and its country.
#The function should return a string formatted like this "Santiago, Chile"
#Call your function with at least three city-country pairs, and print the values that are returned.

def city_country(city, country):
    """Returns the name of a city and its country, neatly formatted"""
    city_and_country = f"{city}, {country}"
    return city_and_country.title()

city_1 = city_country('caracas', 'venezuela')
print(city_1)
city_2 = city_country('madrid', 'spain')
print(city_2)
city_3 = city_country('tokyo', 'japan')
print(city_3)