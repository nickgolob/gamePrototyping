import pygame
import constants
import game.entities.entityBase

class CharacterBase(game.entities.entityBase.EntityBase):
	""" Base class for any moving/'thinking' or controllable game entity """
	
	""" ------------------------ Attributes: -------------------------- """
	
	
	""" ------------------------ Constructors: ------------------------ """
	def __init__(self, x, y):
	
		# call parent constructor
		game.entities.entityBase.EntityBase.__init__(self, x, y)
	
	
	""" ------------------------ Methods: ----------------------------- """