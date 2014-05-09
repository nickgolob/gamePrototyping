import pygame

import constants

from game.entities.entityBase import EntityBase
import game.entities.hitBox

class Baddy(EntityBase):
    ID = 'baddy'

    # baddy type
    type = None

    target = None


    # -- MOVEMENT:
    direct = None # current direction
    transit = 0 # timer denoting number of frames left in transit
                # other movement should not be processed while transitting
    transit_break = 0 # cooldown after transition, rotation
    sourceX, sourceY = 0, 0 # transition source

    hp = 1
    dead = False
    death_timer = 0

    hitBox = None  # sprite representing hit box

    def __init__(self, x, y, type, player):
        """ current types are 'demon' and 'knight'  """

        # initialize parent, load frames into visual sprite component
        keys = ('death', 'demon', 'knight')
        EntityBase.__init__(self, x, y, 'content/proto-battle.png',
            [(constants.BW*3*(i+1), 0, constants.BW*3, constants.BW*3,
              constants.BW*constants.SF, constants.BW*constants.SF, keys[i])
            for i in range(3)])
        self.type = type
        self.visual.setFrame(type)

        self.target = player

        self.hitBox = game.entities.hitBox.HitBox()


    def update(self):
        if self.death_timer > 0:
            self.deathUpdate()

        if not self.dead:
            if self.transit_break == 0:
                moved = False
                if not moved and self.rect.x < self.target.rect.x:
                    self.setHitBox('Right')
                    if not moved and not pygame.sprite.spritecollide(self.hitBox, self.groups()[0], False):
                        moved = True
                        self.direct = 'Right'
                elif not moved and self.rect.x > self.target.rect.x:
                    self.setHitBox('Left')
                    if not moved and not pygame.sprite.spritecollide(self.hitBox, self.groups()[0], False):
                        moved = True
                        self.direct = 'Left'
                if not moved and self.rect.y > self.target.rect.y:
                    self.setHitBox('Up')
                    if not moved and not pygame.sprite.spritecollide(self.hitBox, self.groups()[0], False):
                        moved = True
                        self.direct = 'Up'
                elif not moved and self.rect.y < self.target.rect.y:
                    self.setHitBox('Down')
                    if not moved and not pygame.sprite.spritecollide(self.hitBox, self.groups()[0], False):
                        moved = True
                        self.direct = 'Down'
                if not moved:
                    self.setHitBox('Right')
                    if not moved and not pygame.sprite.spritecollide(self.hitBox, self.groups()[0], False):
                        moved = True
                        self.direct = 'Right'
                elif not moved:
                    self.setHitBox('Left')
                    if not moved and not pygame.sprite.spritecollide(self.hitBox, self.groups()[0], False):
                        moved = True
                        self.direct = 'Left'
                if not moved:
                    self.setHitBox('Up')
                    if not moved and not pygame.sprite.spritecollide(self.hitBox, self.groups()[0], False):
                        moved = True
                        self.direct = 'Up'
                elif not moved:
                    self.setHitBox('Down')
                    if not moved and not pygame.sprite.spritecollide(self.hitBox, self.groups()[0], False):
                        moved = True
                        self.direct = 'Down'
                if moved:
                    self.transit = constants.BADDY_TRANSIT_TIME
                    self.transit_break = constants.BADDY_TRANSIT_TIME + constants.BADDY_TRANSIT_COOL_TIME
                    self.sourceX, self.sourceY = self.rect.x, self.rect.y

            if self.transit_break > 0:
                self.transit_break -= 1
                if self.transit > 0:
                    self.transit -= 1
                    # redraw
                    factor = int(constants.SCALE_FACTOR * constants.BOX_WIDTH *
                                 (1 - self.transit / constants.BADDY_TRANSIT_TIME))
                    if self.direct == 'Left':
                        self.rect.x = self.sourceX - factor
                    elif self.direct == 'Down':
                        self.rect.y = self.sourceY + factor
                    elif self.direct == 'Right':
                        self.rect.x = self.sourceX + factor
                    elif self.direct == 'Up':
                        self.rect.y = self.sourceY - factor
                    self.visual.setFrame(self.type)





    def setHitBox(self, direction):
        self.hitBox.rect.x = self.rect.x
        self.hitBox.rect.y = self.rect.y
        if direction == 'Left':
            self.hitBox.rect.x -= constants.BOX_WIDTH * constants.SCALE_FACTOR
        elif direction == 'Down':
            self.hitBox.rect.y += constants.BOX_WIDTH * constants.SCALE_FACTOR
        elif direction == 'Right':
            self.hitBox.rect.x += constants.BOX_WIDTH * constants.SCALE_FACTOR
        elif direction == 'Up':
            self.hitBox.rect.y -= constants.BOX_WIDTH * constants.SCALE_FACTOR



    def damage(self, amount):
        self.hp -= 1
        if self.hp == 0:
            self.death()


    def death(self):
        if not self.dead:
            self.target.killCount += 1
            self.dead = True
            self.death_timer = constants.BADDY_DEATH_TIME
    def deathUpdate(self):
        self.death_timer -= 1
        if self.death_timer == 0:
            self.kill()
        else:
            self.visual.setFrame('death')