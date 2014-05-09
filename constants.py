""" GAME CONSTANTS """

##################### GAME #####################
CLOCK_RATE = 60

##################### SCREEN / SIZES #####################
SCALE_FACTOR = SF = 4 # scale every measurement in pixels by this amount

BOX_WIDTH = BW = 13 # tile size
S_BOX_WIDTH = S_BW = BW * SF

SPRITE_WIDTH = SW = 13 # standard spite image width
S_SPRITE_WIDTH = S_SW = SW * SF

SPRITE_HEIGHT = SH = 23 # standard sprite image heigh
S_SPRITE_HEIGHT = S_SH = SH * SF

SCREEN_WIDTH = W = S_BW * 20   # Screen dimensions are a set number of tiles
SCREEN_HEIGHT = H = S_BW * 13


##################### SPRITES #####################
COLOR_KEY = (255, 255, 255) # ignores this color when loading images
NUM_SUB_LAYERS = 2 # number of sub layers per tile (values should be from 0 - NUM_SUB_LAYERS - 1)


##################### PLAYER #####################
PLAYER_TRANSIT_TIME = PTF = 8 # how many frames it takes to transition to an adjacent tile
PLAYER_TRANSIT_COOL_TIME = PTCT = 1
PLAYER_REDIRECT_COOL_TIME = 6
PLAYER_SWORD_TIME = PST = 10
PLAYER_SWORD_COOL_TIME = PSCT = 0
PLAYER_DEATH_TIME = 250 # how many frames to display death animation


##################### BADDIES #####################
BADDY_TRANSIT_TIME = BTF = 15 # how many frames it takes to transition to an adjacent tile
BADDY_TRANSIT_COOL_TIME = BTCT = 4
BADDY_DEATH_TIME = 80
