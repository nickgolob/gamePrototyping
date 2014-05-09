


import game.entities.entityBase
import game.entities.hitBox

class CharacterBase(game.entities.entityBase.EntityBase):

    hitBox = None  # sprite representing hit box, used for probing

    def __init__(self, x, y, sheetFile, infoList, transitSpeed): # these variables get transfered directly entityBase
        game.entities.entityBase.EntityBase.__init__(x, y, sheetFile, infoList)

        self.hitBox = game.entities.hitBox.HitBox(self)

