people = []

person_1 = {'first_name': 'Dwayne', 'last_name': 'Johnson', 'age': 48, 'city': 'Southwest Ranches'}
people.append(person_1)

person_2 = {'first_name': 'Zinedine', 'last_name': 'Zidane', 'age': 48, 'city': 'Madrid'}
people.append(person_2)

person_3 = {'first_name': 'Cristiano', 'last_name': 'Ronaldo', 'age': 36, 'city': 'Turin'}
people.append(person_3)

people = [person_1, person_2, person_3]

for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"

    age = person['age']

    city = person['city'].title()
    
    print(f"{name}, of {city}, is {age} years old.")