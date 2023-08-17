from dino_runner.utils.constants import SERRA, SERRA_TYPE
from dino_runner.components.power_ups.power_up import PowerUp

class Serra(PowerUp):
    def __init__(self):
        self.image = SERRA
        self.type = SERRA_TYPE
        super().__init__(self.image, self.type)
