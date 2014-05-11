import constants
import game.entitities.entityBase

class Tile(game.entities.entityBase.EntityBase):
	""" generic tile class, used for generally static game entities """
	ID = 'tile'
	
	""" ------------------------ Attributes: -------------------------- """
	passable = True # attribute determining if characters may cross tile
	
	""" ------------------------ Constructors: ------------------------ """
	def __init__(self, x, y, tileKey):
	
		# initialize parent
		game.entities.entityBase.EntityBase.__init__(self, x, y)
		
		# load a single frame, based on tileKey
		# @@@@@@ need to do this
		
		# self.visual.setFrame(keys[tileNum])
		
	
	""" ------------------------ Methods: ----------------------------- """