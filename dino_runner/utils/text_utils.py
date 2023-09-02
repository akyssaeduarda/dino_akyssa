import pygame 

from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, TEXT_COLOR_DARK_GREY

FONT_COLOR = TEXT_COLOR_DARK_GREY
FONT_SIZE = 20
FONT_STYLE = "./dino_runner/assets/font/dinoFont.ttf"


def draw_message_component(
        message,
        screen, 
        font_color = FONT_COLOR,
        font_size = FONT_SIZE,
        font_style = FONT_STYLE,
        pos_x_center = SCREEN_WIDTH // 2,
        pos_y_center = SCREEN_HEIGHT // 2,
):
    font = pygame.font.Font(font_style, font_size)
    text = font.render(message, True, font_color)
    text_rect = text.get_rect()
    text_rect.center = (pos_x_center, pos_y_center)
    screen.blit(text, text_rect)