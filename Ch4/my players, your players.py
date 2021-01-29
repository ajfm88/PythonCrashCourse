my_players = ['zidane', 'figo', 'beckham', 'raul', 'r carlos', 'nedved', 'e davis', 'van nistelrooy', 'ronaldo']
friends_players = my_players[:]

my_players.append('thuram')
friends_players.append('nesta')

print("My team's players are:")
for players in my_players:
      print(f"- {players}")

print("\nMy friend's team's players are:")
for players in friends_players:
      print(f"- {players}")

print("test")