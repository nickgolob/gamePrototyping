
import pygame

import constants

from game.utilities.spriteSheetFunctions import SpriteSheet
from game.entities.imageSpriteComponent import ImageSpriteComponent

class EntityBase(pygame.sprite.Sprite):
	""" All in game entities should use this base class,
		which initializes to a null image sprite for game
		logic, and references as an actual sprite for visuals.
		
		The in game coordinates for the sprite should be
		(self.rect.x, self.rect.y)
	"""
    ID = 'base' # all entities should use an ID

    visual = None # ImageSpriteComponent

    def __init__(self, x, y):
    	""" sets up actual sprite box, does not load frames """

        pygame.sprite.Sprite.__init__(self)
        nullImageSheet = SpriteSheet('content/null-tile.png')
        self.image = pygame.transform.scale(nullImageSheet.get_image(
            0, 0, constants.BOX_WIDTH, constants.BOX_WIDTH),
            (constants.S_BOX_WIDTH, constants.S_BOX_WIDTH))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.visual = ImageSpriteComponent(self)

    def get_frames(self, sheetFile, *frameTuples):
        """ Takes a file containing a sprite sheet (sheetFile) and a list
            of tuples (infoList) designating sprites from the sprite sheet
            to be loaded. The tuple must have the following info ordered
            respectively: (x, y, width, height, rx, ry, key).

            sheetFile must be a string with file name RELATIVE FROM
            entityBase.py

            - x, y - coordinates to upper left point of sprite on sheet
            - width, height - dimensions in pixels of sprite
            - ry, rx - reference coordinates for display relative to sprite image
                (corresponding to top left corner point of actual sprite)
            - key - value to reference sprite by
        """

        sprite_sheet = SpriteSheet(sheetFile)
        for frame in frameTuples:
            self.visual.frames[frame[6]] = (
                pygame.transform.scale(
                    sprite_sheet.get_image(frame[0], frame[1], frame[2], frame[3]),
                    (frame[4] * constants.SCALE_FACTOR, frame[5] * constants.SCALE_FACTOR)),
                frame[4], frame[5])

    def kill(self):
    	""" this overrides the sprite kill function, to also call 'kill'
    		on the visual component """
        pygame.sprite.Sprite.kill(self)
        self.visual.kill()