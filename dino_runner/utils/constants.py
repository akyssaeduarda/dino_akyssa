import pygame
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

#cores textos
TEXT_COLOR_DARK_GREY = ("#535353")
TEXT_COLOR_LIGHT_GRAY = ("#737373")
TEXT_COLOR_RED = ("#6A040F")
TEXT_COLOR_GREEN = ("#283618")

#musicas
pygame.init()
pygame.mixer.music.set_volume(0.03)
MUSIC_FUNDO = pygame.mixer.music.load(os.path.join(IMG_DIR, "music/music_fundo.mp3"))
JUMPING_MUSIC = pygame.mixer.Sound(os.path.join(IMG_DIR, "music/jump_music.wav"))

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))
GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, "Other/GameOver.png"))

# Dino
DINO_START = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoStart.png"))
DINO_DEAD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead.png"))

# Run
RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRun2.png")),
]
RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRunShield1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRunShield2.png")),
]
RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRunHammer1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRunHammer2.png")),
]
RUNNING_SERRA = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRunSerra1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRunSerra2.png")),
]

# Duck
DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/DinoDuck2.png")),
]
DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/DinoDuckShield1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/DinoDuckShield2.png")),
]
DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/DinoDuckHammer1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/DinoDuckHammer2.png")),
]
DUCKING_SERRA = [
   pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/DinoDuckSerra1.png")), 
   pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/DinoDuckSerra2.png")), 
]

# Jump
JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/Jump/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(
    os.path.join(IMG_DIR, "Dino/Jump/DinoJumpShield.png")
)
JUMPING_HAMMER = pygame.image.load(
    os.path.join(IMG_DIR, "Dino/Jump/DinoJumpHammer.png")
)
JUMPING_SERRA = pygame.image.load(
    os.path.join(IMG_DIR, "Dino/Jump/DinoJumpSerra.png")
)

# Obstacles
SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]
BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]
ROCHA = [
    pygame.image.load(os.path.join(IMG_DIR, "Rocha/Rocha1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Rocha/Rocha2.png")),
]

# Doodads
CLOUD = pygame.image.load(os.path.join(IMG_DIR, "Other/Cloud.png"))

# Power ups
SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Other/Shield.png"))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Other/Hammer.png"))
SERRA = pygame.image.load(os.path.join(IMG_DIR, "Other/Serra.png"))


BG = pygame.image.load(os.path.join(IMG_DIR, "Other/Track.png"))
HEART = pygame.image.load(os.path.join(IMG_DIR, "Other/SmallHeart.png"))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = 'hammer'
SERRA_TYPE = 'serra'
