#First, we import the sys and pygame modules. The pygame module con­
#tains the functionality we need to make a game. We’ll use tools in the sys
#module to exit the game when the player quits.

import sys

import pygame

from settings import Settings
from ship import Ship

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

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
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

        self.ship = Ship(self)
        #We import Ship and then make an instance of Ship after the screen has been created
        #The call to Ship() requires one argument, an instance of AlienInvasion. The self
        #argument here refers to the current instance of AlienInvasion.
        #This is the paramenter that gives Ship access to the game's resources,
        #such as the screen object. We assign this Ship instance to self.ship

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
            self._check_events()
            #Checking for new events.
            self.ship.update()
            #The ship’s position will be updated after we’ve checked for keyboard
            #events and before we update the screen. This allows the ship’s position to be
            #updated in response to player input and ensures the updated position will
            #be used when drawing the ship to the screen.
            self._update_screen()
            #Updating the screen on each pass through the loop.

    def _check_events(self):
        """Respond to keypresses and mouse events."""
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
        #and we call sys.exit() to exit the game.
            elif event.type == pygame.KEYDOWN:
            #Inside _check_events() we add an elif block to the event loop to respond
            #when Pygame detects a KEYDOWN event
                if event.key == pygame.K_RIGHT:
                #We check whether the key pressed,
                #event.key, is the right arrow key
                    #Move the ship to the right.
                    self.ship.moving_right = True
                    #we modify how the game responds when the player presses the
                    #right arrow key: instead of changing the ship’s position directly, we merely
                    #set moving_right to True.
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                    #If a KEYDOWN event occurs for the K_LEFT key, we set moving_left to True. If a
                    #KEYUP event occurs for the K_LEFT key, we set moving_left to False. We can use
                    #elif blocks here because each event is connected to only one key. If the player
                    #presses both keys at once, two separate events will be detected.
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                    #we add a new elif block, which responds to
                    #KEYUP events. When the player releases the right arrow key 
                    #(K_RIGHT), we set moving_right to False.
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        #Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        #we fill the screen with the background color using the fill()method, 
        #which acts on a surface and takes only one argument: a color.
        #WE use self.settings to access the background color when filling the screen
        self.ship.blitme()
        #After filling the background, we draw the ship on the screen by calling
        #ship.blitme, so the ship appears on top of the background.

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