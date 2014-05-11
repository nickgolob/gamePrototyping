import pygame
import constants
import game.entities.entityBase
import game.entities.hitbox

class CharacterBase(game.entities.entityBase.EntityBase):
	""" Base class for any moving/'thinking' or controllable game entity """
	
	""" ------------------------ Attributes: -------------------------- """
	hitBox = None  # sprite representing hit box, used for probing
	
	""" ------------------------ Constructors: ------------------------ """
	def __init__(self, x, y):
	
		# call parent constructor
		game.entities.entityBase.EntityBase.__init__(self, x, y)
		
		# instantiate hitbox
		self.hitbox = game.entities.hitBox.Hitbox(self)
	
	
	""" ------------------------ Methods: ----------------------------- """