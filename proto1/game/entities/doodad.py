
import game.entities.entityBase

class Doodad(game.entities.entityBase.EntityBase):
    ID = 'doodad'

    def __init__(self, x, y, type):

        keys = ['wall']

        infoList = [(0, constants.SPRITE_HEIGHT * 2, constants.SW,
                         constants.SH, 0, (constants.SH - constants.BW)* constants.SCALE_FACTOR,
                         keys[tileNum] )]
