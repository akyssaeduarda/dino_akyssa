import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import ROCHA


class Rocha(Obstacle):
    def __init__(self):
         self.type = random.randint(0, 1)
         super().__init__(ROCHA, self.type)
         self.rect.y = 360        