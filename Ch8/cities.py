#Write a function called describe_city() that accepts the name of a city and its country.
#The function should print a simple sentence, such as
#Caracas is in Venezuela.
#Give the parameter for country a default value.
#Call your function for three different cities, at least one of which is not in the default country.

def describe_city(city, country='USA'):
    """Display information about a city and its country"""
    print(f"\n{city} is in {country}.")

describe_city('New York')
describe_city('St. Louis')
describe_city('Paris', 'France')