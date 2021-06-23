players = ['c ronaldo', 'zidane', 'figo', 'beckham', 'messi']
message = f"My favorite soccer player is {players[1].title()}"
print(message)

players.append('ibrahimovic')
print(players)

players.insert(1, 'ronaldinho')
print(players)

message = f"My favorite soccer player is {players[1].title()}"
print(message)

cars = ['audi', 'bmw', 'subaru']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        