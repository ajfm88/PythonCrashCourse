guests = ['hideo', 'miyamoto', 'sakurai']

print(f"Even though MGS 5 was just okay, I'd like to invite you to dinner, Mr. {guests[0].title()}.")

print(f"You've truly set yourself apart in the industry, I'd like to invite you to dinner, Mr. {guests[1].title()}.")

print(f"I loved SSB for the 3DS. I'd also like to extend you an invitation, Mr. {guests[2].title()}.")


print(f"Unfortunately, Mr. {guests[2].title()} cannot make it.")


del guests[2]


guests.insert(2, 'tajiri')


newfirstguest = f"Once more, I'd like to invite you to dinner, Mr. {guests[0].title()}."
print(newfirstguest)

newsecondguest = f"Once more, I'd like to invite you to dinner, Mr. {guests[1].title()}."
print(newsecondguest)

newthirdguest = f"I'd like to also invite you to dinner, Mr. {guests[2].title()}."
print(newthirdguest)

print ("I found a bigger dinner table!")

guests.insert(0, 'toriyama')

guests.insert(2, 'mikami')

guests.append('aonuma')

newfourthguest = f"I'd like to also invite you, Mr. {guests[0].title()}."
print(newfourthguest)

newfifthguest = f"It would be great if you could join us, Mr. {guests[2].title()}."
print(newfifthguest)

newsixthguest = f"Please feel free to join the fun, Mr. {guests[5].title()}."
print(newsixthguest)

print("My dinner table won't arrive in time for dinner, I only have space for two people.")


uninvited1=guests.pop(5)
print(f"Sorry, but I can no longer host you Mr. {uninvited1.title()}.")

uninvited2=guests.pop(4)
print(f"Sorry, but there are no more spaces for dinner, Mr. {uninvited2.title()}.")

uninvited3=guests.pop(3)
print(f"Sorry, but dinner is no longer an option, Mr. {uninvited3.title()}.")

uninvited4=guests.pop(2)
print(f"There is no such thing as free dinner, Mr. {uninvited4.title()}.")

newfirstguest = f"There is still dinner at my place, Mr. {guests[1].title()}."
print(newfirstguest)

newsecondguest = f"There is still dinner at my place, Mr. {guests[0].title()}."
print(newsecondguest)

del guests[1]
del guests[0]
print(guests)
