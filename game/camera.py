
import constants

class Camera():
    """ Camera class will control most
        drawing functionality

        Is focused on the player """

	""" ------------------------ Attributes: -------------------------- """
    player = None # reference to player, to which it will center around
    x, y = 0, 0   # coordinates of camera (upper left as usual)
	
	""" ------------------------ Constructors: ------------------------ """
    def __init__(self, player):

        self.player = player
        self.center()
    
    """ ------------------------ Methods: ----------------------------- """
    def center(self):
    	""" re-centers camera coordinates over player """
        self.x = self.player.x - (constants.SCREEN_TILE_COLS // 2) * constants.S_BW
        self.y = self.player.y - (constants.SCREEN_TILE_ROWS // 2) * constants.S_BW
        
    def update(self):
    	self.center()

	
