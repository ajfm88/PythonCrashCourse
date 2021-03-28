#First, we import the sys and pygame modules. The pygame module con­
#tains the functionality we need to make a game. We’ll use tools in the sys
#module to exit the game when the player quits.

import sys

import pygame

#Alien Invasion starts as a class called AlienInvasion. 

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

#In the __init__() method, the pygame.init() function initializes the background settings that
#Pygame needs to work properly

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        #We import Settings into the main program file. Then we create an
        #instance of Settings and assign it to self.settings

        self.screen = pygame.display.set_mode(
            (self.settings.screen_Width, self.settings.screen_height))
        #When we create a screen, we use the screen_width and
        #screen_height attributes of self.settings, 

        #we call pygame.display.set_mode() to create a display window, 
        # on which we’ll draw all the game’s graphical ele­ments.

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

#The argument (1200, 800) is a tuple that defines the dimensions of
#the game window, which will be 1200 pixels wide by 800 pixels high. (You
#can adjust these values depending on your display size.) We assign this dis­
#play window to the attribute self.screen, so it will be available in all methods
#in the class.

        #Set the background color.
        self.bg_color = (230, 230, 230)


#The game is controlled by the run_game() method. This method contains
#a while loop that runs continually. The while loop contains an event loop
#and code that manages screen updates.
#An event is an action that the user performs while playing the game, 
#such as pressing a key or moving the mouse. To make our program respond to 
#events, we write this event loop to listen for events and perform 
#appropriate tasks depending on the kinds of events that occur.
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse movements.
            # This for loop is an event loop.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
#To access the events that Pygame detects, we’ll use the pygame.event.get() function.
#This function returns a list of events that have taken place
#since the last time this function was called. Any keyboard or mouse event
#will cause this for loop to run. Inside the loop, we’ll write a series of if
#statements to detect and respond to specific events. For example, when the
#player clicks the game window’s close button, a pygame.QUIT event is detected
#and we call sys.exit() to exit the game 

            #Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            #we fill the screen with the background color using the fill()method, 
            #which acts on a surface and takes only one argument: a color.
            #WE use self.settings to access the background color when filling the screen

            #Make the most recently drawn screen visible.
            pygame.display.flip()

#The call to pygame.display.flip() tells Pygame to make the most
#recently drawn screen visible. In this case, it simply draws an empty screen
#on each pass through the while loop, erasing the old screen so only the new
#screen is visible. When we move the game elements around, pygame.display.flip()
#continually updates the display to show the new positions of game
#elements and hides the old ones, creating the illusion of smooth movement.

if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

#At the end of the file, we create an instance of the game, and then call
#run_game(). We place run_game() in an if block that only runs if the file is
#called directly. When you run this alien_invasion.py file, you should see an
#empty Pygame window.