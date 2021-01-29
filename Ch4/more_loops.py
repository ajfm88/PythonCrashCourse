players = ['zidane', 'figo', 'beckham', 'raul', 'r carlos', 'nedved', 'e davis', 'van nistelrooy', 'ronaldo']

print("Here are the first three players on my team:")

for player in players[:3]:
      print(player.title())

print("Here are the middle three players on my team:")

for player in players[3:6]:
    print(player.title())

print("Here are the last three players on my team:")

for player in players[6:10]:
    print(player.title())
