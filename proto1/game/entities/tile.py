

import constants

from game.entities.entityBase import EntityBase

class Tile(EntityBase):
    ID = 'tile'

    def __init__(self, x, y, tileNum):

        rowsInSpriteSheet = rows = 2
        colsInSpriteSheet = cols = 4
        numGrassTiles = 8

        # load frames into visual sprite component
        keys = ['grass' + str(i) for i in range(numGrassTiles)] + ['wall']
        # initialize parent, only load one initial frame for tile
        infoList = [(0 + constants.SPRITE_WIDTH * (tileNum % cols),
                     0 + constants.SPRITE_HEIGHT * (tileNum // cols),
                     constants.BOX_WIDTH, constants.BOX_WIDTH, 0, 0, keys[tileNum])]

        EntityBase.__init__(self, x, y, 'content/proto-tilesheet.png', infoList)
        # set the frame
        self.visual.setFrame(keys[tileNum])

