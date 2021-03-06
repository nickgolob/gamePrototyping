
import pygame

import constants

from game.utilities.spriteSheetFunctions import SpriteSheet
from game.entities.imageSpriteComponent import ImageSpriteComponent


class EntityBase(pygame.sprite.Sprite):
    ID = 'base'

    visual = None # ImageSpriteComponent

    def __init__(self, x, y, sheetFile, infoList):

        # initualize actual sprite
        pygame.sprite.Sprite.__init__(self)
        nullImageSheet = SpriteSheet('content/null-tile.png')
        self.image = pygame.transform.scale(nullImageSheet.get_image(
            0, 0, constants.BOX_WIDTH, constants.BOX_WIDTH),
            (constants.S_BOX_WIDTH, constants.S_BOX_WIDTH))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # initialize visual sprite, giving reference to actual (self)
        self.visual = ImageSpriteComponent(self)
        self.getFrames(sheetFile, infoList)


    def getFrames(self, sheetFile, infoList):
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
        for imgInfo in infoList:
            self.visual.frames[imgInfo[6]] = [
                pygame.transform.scale(
                    sprite_sheet.get_image(imgInfo[0], imgInfo[1], imgInfo[2], imgInfo[3]),
                    (imgInfo[2]*constants.SCALE_FACTOR, imgInfo[3]*constants.SCALE_FACTOR)),
                imgInfo[4], imgInfo[5]]

    def kill(self): # override to kill self, and visual component
        pygame.sprite.Sprite.kill(self)
        self.visual.kill()
