import pygame
import constants
import game.utilities.spriteSheetFunctions

class Hitbox(pygame.sprite.Sprite):
	""" hitbox is an empty sprite that can be used to check collisions """
	
	""" ------------------------ Attributes: -------------------------- """
	actualRef = None # reference to actual
	
	""" ------------------------ Constructors: ------------------------ """
	def __init__(self):
	
		pygame.sprite.Sprite.__init__(self)
        nullImageSheet = SpriteSheet('content/null-tile.png')
        self.image = pygame.transform.scale(nullImageSheet.get_image(
            0, 0, constants.BOX_WIDTH, constants.BOX_WIDTH),
            (constants.S_BOX_WIDTH, constants.S_BOX_WIDTH))
        self.rect = self.image.get_rect()
	
	""" ------------------------ Methods: ----------------------------- """
	def quick_set(self, direction):
        """ sets hit one tile adjecent in the specified direction from parent """
        self.rect.x = self.actualRef.rect.x
        self.rect.y = self.actualRef.rect.y
        if direction == constants.LEFT:
            self.rect.x -= constants.S_BOX_WIDTH
        elif direction == constants.DOWN:
            self.rect.y += constants.S_BOX_WIDTH
        elif direction == constants.RIGHT:
            self.rect.x += constants.S_BOX_WIDTH
        elif direction == constants.UP:
            self.rect.y -= constants.S_BOX_WIDTH