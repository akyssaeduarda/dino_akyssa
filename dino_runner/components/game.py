import pygame

from dino_runner.utils.constants import BG, ICON, GAME_OVER, DINO_START, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE,TEXT_COLOR_LIGHT_GRAY, GAME_OVER_MUSIC
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.text_utils import draw_message_component


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
        self.best_score = 0
        self.death_count = 0
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        GAME_OVER_MUSIC.stop()
        pygame.mixer.music.play(-1)
        self.playing = True
        self.score = 0
        self.game_speed = 20
        self.player.type = DEFAULT_TYPE
        self.player.has_power_up = False
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.resert_power_ups()
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
        self.power_up_manager.update(self)
        self.update_score()
    
    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 3
        
        if self.score > self.best_score:
            self.best_score = self.score

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_score()
        self.draw_power_up_time()
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

    def draw_score(self):
        draw_message_component(
            f" HI:{self.best_score:05}",
            self.screen,
            pos_x_center = 870,
            pos_y_center = 50,
            font_size = 15,
            font_color= TEXT_COLOR_LIGHT_GRAY,
        )
        draw_message_component(
            f"{self.score:05}",
            self.screen,
            pos_x_center = 1000,
            pos_y_center = 50,
            font_size = 15,
        )

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 1)
            if time_to_show >= 0:
                draw_message_component(
                    f"{self.player.type.capitalize()} enable for {time_to_show} seconds",
                    self.screen,
                    font_size = 18,
                    pos_x_center = 550,
                    pos_y_center = 90,
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def show_menu(self):
        
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2 

        if self.death_count == 0:   # Tela de inicio
            self.screen.fill((255,255,255))
            self.screen.blit(DINO_START, (half_screen_width - 40, half_screen_height - 140))
            
            draw_message_component(
                "Press space to start",
                self.screen,
            )
            draw_message_component(
                "Hammer removes stone | Shield removes bird | Saw removes cactus",
                self.screen,
                pos_y_center = half_screen_height + 60,
                font_size = 15,
            )
        else: # Tela de restart
            self.screen.blit(GAME_OVER, (half_screen_width - 192, half_screen_height - 140))
            
            draw_message_component(
                "Press space to start", 
                self.screen,
                pos_y_center=half_screen_height - 50,
                font_color = "#313131"

            )
            # draw_message_component(
            #     f"Best Score:{self.best_score}",
            #     self.screen,
            #     pos_x_center = 930,
            #     pos_y_center = 85,
            #     font_size = 15,
            #     font_color= TEXT_COLOR_LIGHT_GRAY,
            # )
            # draw_message_component(
            #     f"Your Score:{self.score}",
            #     self.screen,
            #     pos_x_center = 930,
            #     pos_y_center = 115,
            #     font_size = 15,
            # )
            draw_message_component(
                f"Death Count: {self.death_count}",
                self.screen,
                pos_y_center = half_screen_height + 20,
                font_size = 15,
                

            )
            
        pygame.display.update()
        self.handle_events_on_menu()

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                 self.run()