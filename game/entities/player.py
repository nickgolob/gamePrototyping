import pygame
import constants
import game.entities.characterBase

class Player(game.entitities.characterBase.CharacterBase):
	""" """
	ID = 'player'
	
	""" ------------------------ Attributes: -------------------------- """
	
	""" ------------------------ Constructors: ------------------------ """
	def __init__(self, x, y):
	
		# initialize parent
		game.entitities.characterBase.CharacterBase.__init__(self, x, y)
		
		# load initial frames into visual component
		import itertools.chain # for concatenating generators
		keys = ('standRight', 'standDown', 'standLeft', 'standUp',
                'standRightSword', 'standDownSword', 'standLeftSword', 'standUpSword',
                'swingRightSword', 'swingDownSword', 'swingLeftSword', 'swingUpSword')
		self.get_frames('content/proto-player.png', * itertools.chain(
			((constants.SW * i, 0, constants.SW, constants.SH, 0,
              (constants.SH - constants.BW) * constants.SF, keys[i])
            for i in range(8)),
            ((constants.BW * 3 * i, 26, constants.BW * 3, constants.BW * 3,
              constants.BW * constants.SF, constants.BW * constants.SF, keys[8 + i])
            for i in range(4))))
        self.getFrames('content/proto-battle.png',
            (constants.BW*3, 0, constants.BW*3, constants.BW*3,
              constants.BW*constants.SF, constants.BW*constants.SF, 'death'))
			
		# set initial stance
		self.direct = constants.DOWN
        self.visual.setFrame(keys[1])
		
	
	""" ------------------------ Methods: ----------------------------- """