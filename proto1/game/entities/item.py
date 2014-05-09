
import pygame

import constants

import game.entities.entityBase
import game.utilities.spriteSheetFunctions

class Item(game.entities.entityBase.EntityBase):
    ID = 'sword'

    def __init__(self, x, y):
        game.entities.entityBase.EntityBase.__init__(self, x, y, 'content/proto-battle.png',
            [(0, 0, 3*constants.BW, 3*constants.BW,
              constants.BW * constants.SF, constants.BW * constants.SF, 'sword')])
        self.visual.setFrame('sword')

