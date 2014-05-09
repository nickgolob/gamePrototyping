
import pygame

import constants

import game.entities.tile
import game.entities.player
import game.entities.baddy
import game.entities.item

def main():

    pygame.init()

    screenSize = [constants.SCREEN_WIDTH * constants.SF,
                  constants.SCREEN_HEIGHT * constants.SF]
    screen = pygame.display.set_mode(screenSize)
    pygame.display.set_caption("TimeCraft -- ProtoType Alpha")


    # ---- PRotoTyping


    # script the board:
    objectGroup = pygame.sprite.Group()
    imageSprites = pygame.sprite.LayeredUpdates()

    backgroundSprites = pygame.sprite.LayeredUpdates()

    boxDim = constants.BOX_WIDTH * constants.SCALE_FACTOR
    for i in range((screenSize[1] // boxDim)):
        wall = game.entities.tile.Tile(0, i*boxDim, 8)
        objectGroup.add(wall)
        imageSprites.add(wall.visual)
        wall = game.entities.tile.Tile((screenSize[0] // boxDim - 1)*boxDim, i*boxDim, 8)
        objectGroup.add(wall)
        imageSprites.add(wall.visual)
        for j in range(screenSize[0] // boxDim):
            if i == 0:
                wall = game.entities.tile.Tile(j*boxDim, 0, 8)
                objectGroup.add(wall)
                imageSprites.add(wall.visual)
                wall = game.entities.tile.Tile(j*boxDim, (screenSize[1] // boxDim - 1)*boxDim, 8)
                objectGroup.add(wall)
                imageSprites.add(wall.visual)
            backgroundSprites.add(game.entities.tile.Tile(
                boxDim*j, boxDim*i, (10*i+j) % 8).visual)


    player = game.entities.player.Player(3*boxDim, 3*boxDim)
    imageSprites.add(player.visual)

    imageSprites.update()

    level = 1
    levelTimer = 0
    # ---- PRotoTyping


    clock = pygame.time.Clock()
    timer = 0

    done = False
    while not done:

        # -- get user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.swing(objectGroup)

        input = pygame.key.get_pressed()
        if input[pygame.K_LEFT]:
            player.go('Left', objectGroup)
        elif input[pygame.K_DOWN]:
            player.go('Down', objectGroup)
        elif input[pygame.K_RIGHT]:
            player.go('Right', objectGroup)
        elif input[pygame.K_UP]:
            player.go('Up', objectGroup)

        # -- game logic
        objectGroup.update()
        player.update()

        for hitSprite in pygame.sprite.spritecollide(player, objectGroup, False):
            if hitSprite.ID == 'baddy' and not hitSprite.dead:
                player.death()
            if hitSprite.ID == 'sword':
                sword.kill()
                player.hasSword = True
                player.visual.setFrame('standDownSword')


        # -- level logic
        if level == 1:
            if levelTimer == 150:
                badguy = game.entities.baddy.Baddy(1*boxDim, 7*boxDim, 'knight', player)
                objectGroup.add(badguy)
                imageSprites.add(badguy.visual)

            if levelTimer == 600: # 600
                sword = game.entities.item.Item(4*boxDim, 4* boxDim)
                objectGroup.add(sword)
                imageSprites.add(sword.visual)
                sword.visual.resetLayer()

            if player.killCount == 1:
                levelTimer = 0
                level = 2

        if level == 2:
            if levelTimer == 150:
                badguy = game.entities.baddy.Baddy(1*boxDim, 1*boxDim, 'knight', player)
                objectGroup.add(badguy)
                imageSprites.add(badguy.visual)
                badguy = game.entities.baddy.Baddy(1*boxDim, 3*boxDim, 'knight', player)
                objectGroup.add(badguy)
                imageSprites.add(badguy.visual)
                badguy = game.entities.baddy.Baddy(1*boxDim, 6*boxDim, 'knight', player)
                objectGroup.add(badguy)
                imageSprites.add(badguy.visual)

            if player.killCount == 4:
                levelTimer = 0
                level = 3
                print('level 3')

        if level == 3:
            if levelTimer == 150:
                badguy = game.entities.baddy.Baddy(1*boxDim, 1*boxDim, 'knight', player)
                objectGroup.add(badguy)
                imageSprites.add(badguy.visual)
                badguy = game.entities.baddy.Baddy(1*boxDim, 6*boxDim, 'knight', player)
                objectGroup.add(badguy)
                imageSprites.add(badguy.visual)
                badguy = game.entities.baddy.Baddy(1*boxDim, 11*boxDim, 'knight', player)
                objectGroup.add(badguy)
                imageSprites.add(badguy.visual)
                badguy = game.entities.baddy.Baddy(19*boxDim, 3*boxDim, 'knight', player)
                objectGroup.add(badguy)
                imageSprites.add(badguy.visual)
                badguy = game.entities.baddy.Baddy(19*boxDim, 4*boxDim, 'knight', player)
                objectGroup.add(badguy)
                imageSprites.add(badguy.visual)
                badguy = game.entities.baddy.Baddy(19*boxDim, 10*boxDim, 'knight', player)
                objectGroup.add(badguy)
                imageSprites.add(badguy.visual)

            if player.killCount == 10:
                levelTimer = 0
                level = 4

        if level == 4:
            constants.PLAYER_SWORD_TIME = 4
            player.hasSword = True
            if levelTimer == 200:
                badguy = game.entities.baddy.Baddy(12*boxDim, 1*boxDim, 'demon', player)
                constants.BADDY_TRANSIT_TIME = 10
                constants.BADDY_TRANSIT_COOL_TIME = 8
                badguy.hp = 5
                objectGroup.add(badguy)
                imageSprites.add(badguy.visual)



        # -- game display
        screen.fill((120,120,160))
        backgroundSprites.draw(screen)
        imageSprites.draw(screen)

        if player.killCount == 11:
            endText = pygame.font.SysFont('helvetica',200)
            renderedText = endText.render("NERD MUCH?",0,(0,200,0))
            textPos = renderedText.get_rect()
            textPos.centerx = screen.get_rect().centerx
            screen.blit(renderedText, textPos)
        if player.dead and player.death_timer == 0:
            endText = pygame.font.SysFont('helvetica',200)
            renderedText = endText.render("YOU LOSE",0,(125,0,0))
            textPos = renderedText.get_rect()
            textPos.centerx = screen.get_rect().centerx
            screen.blit(renderedText, textPos)

        pygame.display.flip()

        clock.tick(constants.CLOCK_RATE)
        timer += 1
        levelTimer += 1


if __name__ == "__main__":
    main()