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

# CONSTRAINTS: these should both be odd number, for centering player
SCREEN_TILE_COLS = 21 # Number of tiles fit horizontally across screen
SCREEN_TILE_ROWS = 13 # Number of tiles fit vertically across screen
SCREEN_WIDTH = W = S_BW * SCREEN_TILE_COLS   # Width of screen in pixels
SCREEN_HEIGHT = H = S_BW * SCREEN_TILE_ROWS  # Height of screen in pixels


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
