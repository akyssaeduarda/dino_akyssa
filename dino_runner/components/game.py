import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

FONT_STYLE = "freesansbold.ttf"
TEXT_COLOR_BLACK = (0, 0, 0)
TEXT_COLOR_ORANGE = ("#F18F01")


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.score = 0
        self.death_count = 0
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.playing = True
        self.score = 0
        self.game_speed = 20
        self.obstacle_manager.reset_obstacles()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
    
    def update_score(self):
        #modificar para adicionar eventos com base no score
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 5

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    
    def format_text(self, text_render, color_text, width_rect, height_rect ): 
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(text_render, True, color_text)
        text_rect = text.get_rect()
        text_rect.center = ( width_rect, height_rect)
        self.screen.blit(text, text_rect)

    def draw_score(self):
        self.format_text(f" Score: {self.score}", TEXT_COLOR_ORANGE, 1000, 50)

    def show_menu(self):
        self.screen.fill((225,255,255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2 

        if self.death_count == 0:   # Tela de inicio
            self.format_text("Press any key to start", TEXT_COLOR_BLACK , half_screen_width, half_screen_height)
        else: # Tela de restart
            self.screen.blit(ICON, (half_screen_width - 40, half_screen_height - 140))
            self.format_text("Press any key to start", TEXT_COLOR_BLACK , half_screen_width, half_screen_height)
            self.format_text(f"Score: {self.score}", TEXT_COLOR_BLACK , half_screen_width , half_screen_height + 40)
            self.format_text(f"Death Count: {self.death_count}", TEXT_COLOR_BLACK , half_screen_width , half_screen_height + 80)
            
        pygame.display.update()
        self.handle_events_on_menu()

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()
    
