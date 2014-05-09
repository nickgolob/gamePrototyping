
import pygame

import constants

from game.entities.entityBase import EntityBase
import game.entities.hitBox

class Player(EntityBase):
    ID = 'player'

    action_break = 0 # global cooldown timer
    direct = None # current direction

    # -- MOVEMENT:
    transit = 0 # timer denoting number of frames left in transit
                # other movement should not be processed while transitting
    transit_break = 0 # cooldown after transition, rotation
    sourceX, sourceY = 0, 0 # transition source

    # -- WEAPON:
    hasSword = False
    slash = 0
    slash_break = 0
    hitBox = None  # sprite representing hit box
    swingDamage = 1
    killCount = 0

    # -- DEATH:
    dead = False
    death_timer = 0 # timer for displaying death animation

    def __init__(self, x, y):

        # initialize parent, load frames into visual sprite component
        keys = ('standRight', 'standDown', 'standLeft', 'standUp',
                'standRightSword', 'standDownSword', 'standLeftSword', 'standUpSword',
                'swingRightSword', 'swingDownSword', 'swingLeftSword', 'swingUpSword')
        EntityBase.__init__(self, x, y, 'content/proto-player.png',
            [(constants.SW*i, 0, constants.SW, constants.SH, 0,
              (constants.SH-constants.BW)*constants.SF, keys[i])
            for i in range(8)] +
            [(constants.BW*3*i, 26, constants.BW*3, constants.BW*3,
              constants.BW*constants.SF, constants.BW*constants.SF, keys[8+i])
            for i in range(4)])
        self.getFrames('content/proto-battle.png',
            [(constants.BW*3, 0, constants.BW*3, constants.BW*3,
              constants.BW*constants.SF, constants.BW*constants.SF, 'death')])
        self.direct = 'Down'
        self.visual.setFrame(keys[1])

        # intialize attributes
        self.hasSword = False

    def update(self):
        if self.action_break > 0:
            self.action_break -= 1
        if self.death_timer > 0:
            self.deathUpdate()
        else:

            if self.transit_break > 0:
                self.goUpdate()

            if self.slash_break > 0:
                self.swingUpdate()



    def resetTimers(self):
        self.action_break = 0
        self.death_timer = 0
        self.transit = 0
        self.transit_break = 0
        self.slash = 0
        self.slash_break = 0



    def go(self, direction, objects):
        if self.transit_break == 0 and self.action_break == 0:
            if direction != self.direct:
                if self.transit_break == 0:
                    self.transit_break = constants.PLAYER_REDIRECT_COOL_TIME
                    self.direct = direction
                    if self.hasSword:
                        param = 'Sword'
                    else:
                        param = ''
                    self.visual.setFrame('stand' + self.direct + param)
            else:
                # check for impending collisions before moving:
                clear = True
                self.setHitBox(self.direct)
                for sprite in pygame.sprite.spritecollide(self.hitBox, objects, False ):
                    if sprite.ID == 'doodad':
                        clear = False
                        break
                if clear:
                    self.action_break = constants.PLAYER_TRANSIT_TIME + constants.PLAYER_TRANSIT_COOL_TIME
                    self.transit = constants.PLAYER_TRANSIT_TIME
                    self.transit_break = constants.PLAYER_TRANSIT_TIME + constants.PLAYER_TRANSIT_COOL_TIME
                    self.direct = direction
                    self.sourceX, self.sourceY = self.rect.x, self.rect.y

    def goUpdate(self):
        self.transit_break -= 1
        if self.transit > 0:
            self.transit -= 1
            # redraw
            factor = int(constants.SCALE_FACTOR * constants.BOX_WIDTH *
                         (1 - self.transit / constants.PLAYER_TRANSIT_TIME))
            if self.direct == 'Left':
                self.rect.x = self.sourceX - factor
            elif self.direct == 'Down':
                self.rect.y = self.sourceY + factor
            elif self.direct == 'Right':
                self.rect.x = self.sourceX + factor
            elif self.direct == 'Up':
                self.rect.y = self.sourceY - factor
            if self.hasSword:
                param = 'Sword'
            else:
                param = ''
            self.visual.setFrame('stand' + self.direct + param)


    def swing(self, targetGroup):
        if self.hasSword:
            if self.action_break == 0:
                self.action_break = constants.PLAYER_SWORD_TIME + constants.PLAYER_SWORD_COOL_TIME
                self.slash = constants.PLAYER_SWORD_TIME
                self.slash_break = constants.PLAYER_SWORD_TIME + constants.PLAYER_SWORD_COOL_TIME

                # check hits
                self.setHitBox(self.direct)
                for spriteHit in pygame.sprite.spritecollide(self.hitBox, targetGroup, False):
                    spriteHit.damage(self.swingDamage)

    def swingUpdate(self):
        self.slash_break -= 1
        if self.slash > 0:
            self.slash -= 1
            if self.slash == 0:
                self.visual.setFrame('stand' + self.direct + 'Sword')
            else:
                self.visual.setFrame('swing' + self.direct + 'Sword')


    def death(self):
        if not self.dead:
            self.dead = True
            self.resetTimers()
            self.death_timer = constants.PLAYER_DEATH_TIME
            self.action_break = constants.PLAYER_DEATH_TIME
    def deathUpdate(self):
        self.death_timer -= 1
        if self.death_timer == 0:
            self.kill()
        else:
            self.visual.setFrame('death')








