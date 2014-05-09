
import pygame

import constants

from game.utilities.spriteSheetFunctions import SpriteSheet

class HitBox(pygame.sprite.Sprite):

    actualRef = None

    def __init__(self, actualRef):

        pygame.sprite.Sprite.__init__(self)
        nullImageSheet = SpriteSheet('content/null-tile.png')
        self.image = pygame.transform.scale(nullImageSheet.get_image(
            0, 0, constants.BOX_WIDTH, constants.BOX_WIDTH),
            (constants.S_BOX_WIDTH, constants.S_BOX_WIDTH))
        self.rect = self.image.get_rect()

    def quickSetHitBox(self, direction):
        """ sets hit one tile adjecent in the specified direction from parent """
        self.rect.x = self.actualRef.rect.x
        self.rect.y = self.actualRef.rect.y
        if direction == 'Left':
            self.rect.x -= constants.S_BOX_WIDTH
        elif direction == 'Down':
            self.rect.y += constants.S_BOX_WIDTH
        elif direction == 'Right':
            self.rect.x += constants.S_BOX_WIDTH
        elif direction == 'Up':
            self.rect.y -= constants.S_BOX_WIDTH
