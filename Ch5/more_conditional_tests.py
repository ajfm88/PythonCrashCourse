#test for equality and inequality with strings
print("Testing for equality and inequality")

player = 'c. ronaldo'
if player == 'c. ronaldo':
    print("we have the best player in our team!")

if player == 'cannavaro':
    print("we don't have the best player in our team!")

#tests using the lower()method
player1 = 'Ronaldo'
print("\nThe next thing will evaluate to False due to wrong capitalization")
print(player1 == 'ronaldo')

print("\nBut then if we use the lower() function and normalize the value, it yields True")
print(player1.lower() == 'ronaldo')

#Numerical tests involving equality and inequality, 
#greater than and less than, greater than or equal to and less than or equal to
age = 18
print("\nNow some numerical tests, is '21' greater than '18'?")
print(age < 21)

print("\nAnd is '17' less than '18'?")
print(age > 17)

#Tests using the and keyword and the or keyword
age_1 = 17
age_2 = 21
age_3 = 25
print("\nNow let's do some and and or expressions")
print("\nThe three ages that we will work with are 17, 21 and 25")
print("\nCan the first two people go out for drinks?")
print(age_1 >= 21 and age_2 >= 21)

print("\nCan the last two people go out for drinks?")
print(age_2 >= 21 and age_3 >= 21)

print("\nAre all three people over the age of 15?")
print (age_1 >15) and (age_2>15) and (age_3>15)

print("\nCan the first person date the third person?")
print (age_1>18) and (age_3>18)

print("\nWhat about the second and third person?")
print (age_2>18) and (age_3>18)
#Test whether an item is in a list
team = ['figo', 'zidane', 'c. ronaldo']
print("\nIs 'zidane' in the team?")
print('zidane' in team)

#Test whether an item is not on a list
print("\nIs 'raul' in the team?")
print('raul' in team)