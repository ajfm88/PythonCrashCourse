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
print(guests)


guests.insert(2, 'tajiri')
print(guests)

newfirstguest = f"Once more, I'd like to invite you to dinner, Mr. {guests[0].title()}."
print(newfirstguest)

newsecondguest = f"Once more, I'd like to invite you to dinner, Mr. {guests[1].title()}."
print(newsecondguest)

newthirdguest = f"I'd like to also invite you to dinner, Mr. {guests[2].title()}."
print(newthirdguest)

