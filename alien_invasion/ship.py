#We import the pygame module before defining the class.
import pygame


class Ship:
    """A class to manage the ship."""

# The __init__() method of Ship takes two parameters: the self reference and a 
# reference to the current instance of the AlienInvasion class.
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        #we assign the screen to an attribute of Ship, so we 
        # can access it easily in all the methods in this class.
        self.screen = ai_game.screen

        #we access the screen’s rect attribute using the get_rect() method 
        #and assign it to self.screen_rect. Doing so allows us to place the ship in the
        #correct location on the screen.
        self.screen_rect = ai_game.screen.get_rect()

        #Calling pygame and give it the location of our ship image.
        #This function returns a surface representing the 
        #ship, which we assign to self.image.
        self.image = pygame.image.load('C:/Users/ajfm88/Sites/python_work/alien_invasion/images/ship.bmp')
        #When the image is loaded, we call get_rect() to access the ship 
        #surface’s rect attribute so we can later use it to place the ship.
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        #We’ll position the ship at the bottom center of the screen. To do so,
        #make the value of self.rect.midbottom match the midbottom attribute of the
        #screen’s rect

        #Movement flag
        self.moving_right = False
        #We add a self.moving_right attribute in the __init__() method and set it
        #to False initially
        self.moving_left = False

    #Then we add update(), which moves the ship right if the flag is True
    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.rect.x += 1
            #The update() method will be called through an instance of
            #Ship, so it’s not considered a helper method.
        if self.moving_left:
            self.rect.x -= 1
            #In update(), we use two
            #separate if blocks rather than an elif to allow the ship’s rect.x value to be
            #increased and then decreased when both arrow keys are held down. This
            #results in the ship standing still. If we used elif for motion to the left,
            #right arrow key would always have priority. 

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
        #we define the blitme() method, which draws the image to the
        # screen at the position specified by self.rect.