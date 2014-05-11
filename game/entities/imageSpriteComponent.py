import pygame
import constants

class ImageSpriteComponent(pygame.sprite.DirtySprite):
    """ This sprite auto-layers, by going through groups
        it is in, and calling the change_layer method.
        Therefore all container groups should have this method.
        Coordinates of this sprite should not be relative
        to the in-game basis, but instead relative to the camera """

    """ Dictionary containing all frames, and reference info
        in following tuple form: (image, rx, ry)*
        rx and ry should be PRE-SCALED
        - key is the name of the image """
    frames = {}

	""" ------------------------ Attributes: -------------------------- """
    actualRef = None # reference to actual representation, now the parent sprite
    cameraRef = None # reference the camera for relative coordinates
    subLayer = 0 # sub layer ordering (between 0 and NUM_SUB_LAYERS)
    currentFrame = None # track dictionary key of current frame

	""" ------------------------ Constructors: ------------------------ """
    def __init__(self, actualRef, cameraRef):
        pygame.sprite.DirtySprite.__init__(self)
        self.actualRef = actualRef
        # get sub layer
        self.subLayer = 0
        if actualRef.ID == 'player': # @@@ this may need to be moved
            self.subLayer = 1
	
	""" ------------------------ Methods: ----------------------------- """
    def load_frame(self, key, frameTuple):
        self.frames[key] = frameTuple

    def set_frame(self, key):
        """ quickset standard frame from actual sprites position """
        self.currentFrame = key
        self.refresh_frame()

    def refresh_frame(self):
    	""" this function does a full tune-up, in preparation for drawing """
        imageTuple = self.frames[self.currentFrame]
        self.image = imageTuple[0]
        self.rect = self.image.get_rect()
        self.refresh_coords() # set correct coordinates 
        self.reset_layer() # set correct layering

    def reset_layer(self):
        """ multi-purpose reset layer function """
        for group in self.groups():
            group.change_layer(self,
            	self.actualRef.rect.y * constants.NUM_SUB_LAYERS + self.subLayer)
            
    def refresh_coords(self):
    	""" get relative coordinates to camera, from actual """
    	imageTuple = self.frames[self.currentFrame] # @@@ redundant call from refresh_frame
    	self.rect.x = self.actualRef.rect.x - imageTuple[1] - self.cameraRef.x
    	self.rect.y = self.actualRef.rect.y - imageTuple[2] - self.cameraRef.y
    	
    	
    	
    	
    	