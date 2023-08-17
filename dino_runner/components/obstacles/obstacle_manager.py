import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.rocha import Rocha


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game): 
        obstacle_type = [
            Cactus(),
            Bird(),
            Rocha(),
        ]
        
        if len(self.obstacles) == 0:
              self.obstacles.append(obstacle_type[random.randint(0, 2)])
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
           
            if game.player.dino_rect.colliderect(obstacle.rect):     
                if game.player.type == 'shield' and isinstance(obstacle, Bird):
                    self.obstacles.remove(obstacle) 
                    if isinstance(obstacle, Cactus) or isinstance(obstacle, Rocha):
                        pygame.time.delay(500)
                        game.playing = False
                        game.death_count += 1
                        break
                elif game.player.type == 'hammer' and isinstance(obstacle, Rocha):
                    self.obstacles.remove(obstacle) 
                    if isinstance(obstacle, Bird) or isinstance(obstacle, Cactus):
                        pygame.time.delay(500)
                        game.playing = False
                        game.death_count += 1
                        break
                elif game.player.type == 'serra' and isinstance(obstacle, Cactus):
                    self.obstacles.remove(obstacle) 
                    if isinstance(obstacle, Bird) or isinstance(obstacle, Rocha):
                        pygame.time.delay(500)
                        game.playing = False
                        game.death_count += 1
                        break
                else:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break
            
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def reset_obstacles(self):
        self.obstacles = []
        
           