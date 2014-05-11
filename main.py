import pygame
import constants

def main():


    # ---- pygame initialization
    pygame.init()
    screenSize = (constants.SCREEN_WIDTH, constants.SPRITE_HEIGHT)
    screen = pygame.display.set_mode(screenSize)
    pygame.display.set_caption('TimeCraft')
    clock = pygame.time.Clock()


    # ---- game initilialization









    # ---- game loop
    timer = 0
    done = False
    while not done:

        # ---- get user input



        # ---- game logic



        # ---- display logic



        # ---- finish
        timer += 1
        clock.tick(constants.CLOCK_RATE)






if __name__ == '__main__':
    main()