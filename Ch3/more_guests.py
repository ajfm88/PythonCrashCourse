guests = ['hideo', 'miyamoto', 'sakurai']

firstguest = f"Even though MGS 5 was just okay, I'd like to invite you to dinner, Mr. {guests[0].title()}."
print(firstguest)

secondguest = f"You've truly set yourself apart in the industry, I'd like to invite you to dinner, Mr. {guests[1].title()}."
print(secondguest)

thirdguest = f"I loved SSB for the 3DS. I'd also like to extend you an invitation, Mr. {guests[2].title()}."
print(thirdguest)


cantmakeit = f"Unfortunately, Mr. {guests[2].title()} cannot make it."
print(cantmakeit)


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
