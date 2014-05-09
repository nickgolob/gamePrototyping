import pygame



class EntityGroup(pygame.sprite.Group):
    """ Modified Group Class

        So far, only overrides the update function
        to update the parent (since images """


    def __init__(self):
        pygame.sprite.Group.__init__(self)

    def update(self, *args):
        for s in self.sprites():
            s.actualRef.update(*args)