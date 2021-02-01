#Turn your if-else chain from alien_colors_2 into an if-elif-else chain
#If the alien is green, print a message that the player earned 5 points.
#If the alien is yellow, print a message that the player earned 10 points.
#If the alien is red, print a messsage that the player earned 15 points.
#Write three versions of this program, 
#making sure each message is printed for the appropriate color alien.

alien_color = 'green'

if alien_color == 'green':
    print("The player has earned 5 points!")

elif alien_color == 'yellow':
    print("The player has earned 10 points!")

elif alien_color == 'red':
    print("The player has earned 15 points!")

#Version 2
alien_color = 'yellow'

if alien_color == 'green':
    points = 5

elif alien_color == 'yellow':
    points = 10

elif alien_color == 'red':
    points = 15

print(f"\nFor this new and improved program. The player has earned {points} points!")

#Version 3
alien_color = 'red'

if alien_color == 'green':
    points = 5

elif alien_color == 'yellow':
    points = 10

elif alien_color == 'red':
    points = 15

print(f"\nThird version. The player has earned {points} points!")