#Choose a color for an alien as you did in exercise 5-3, a nd write an if-else chain
#If the aline's color is green, print a statement that the player just earned 5 points
#If the alien's color isn't green print a statement that the player just earned 10 points
#Write one version of this program that runs the if block and another that runs the else block.

alien_color = 'yellow'
if alien_color == 'green':
    print("Congratulations! You just earned 5 points!")
else:
    print("Congratulations! You just earned 10 points!")

alien_color = 'green'
if alien_color == 'green':
    print("\n\nThis is another game. Congratulations! You just earned 5 points!")
else:
    print("This is another game. Congratulations You just earned 10 points!")
    