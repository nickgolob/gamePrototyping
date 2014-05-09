

import pygame

import constants

class ImageSpriteComponent(pygame.sprite.DirtySprite):
    """ This sprite auto-layers, by going through groups
        it is in, and calling the change_layer method.
        Therefore all container groups should have this method. """


    """ Dictionary containing all frames, and reference info
        in following tuple form: (image, rx, ry)*
        rx and ry should be PRE-SCALED """
    frames = {}

    """ reference pointer to associated actual sprite
        used for quick info on current coordinates via
        references rectangle x,y values """
    actualRef = None # now the parent sprite
    subLayer = 0 # sub layer ordering (between 0 and NUM_SUB_LAYERS)
    currentFrame = None # track dictionary key of current frame

    def __init__(self, actualRef):
        pygame.sprite.Sprite.__init__(self)
        self.actualRef = actualRef
        # get sub layer
        self.subLayer = 0
        if actualRef.ID == 'player':
            self.subLayer = 1

    def loadFrame(self, key, frameTuple):
        self.frames[key] = frameTuple

    def setFrame(self, key):
        """ quickset standard frame from actual sprites position """
        self.currentFrame = key
        self.refreshFrame()

    def refreshFrame(self):
        imageTuple = self.frames[self.currentFrame]
        self.image = imageTuple[0]
        self.rect = self.image.get_rect()
        # get coordinated from actual
        self.rect.x = self.actualRef.rect.x - imageTuple[1] # x-offset
        self.rect.y = self.actualRef.rect.y - imageTuple[2] # y-offset
        # set correct layering
        self.resetLayer()

    def resetLayer(self):
        """ multi-purpose reset layer function """
        for group in self.groups():
            group.change_layer(self, self.actualRef.rect.y*constants.NUM_SUB_LAYERS + self.subLayer)





