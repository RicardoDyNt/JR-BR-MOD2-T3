import random
from time import time
import pygame

from dino_runner.components.powerups.shield import Shield 
from dino_runner.components.powerups.hammer import Hammer
from dino_runner.components.powerups.time import Time
from dino_runner.utils.constants import HAMMER_TYPE, SHIELD_TYPE, TIME_TYPE


POWER_UPS = [
    Shield(),
    Hammer(),
    Time(),
    ]


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(200, 300)
            self.power_ups.append(POWER_UPS[random.randint(0,2)])

    def update(self, score, game_speed, player):
        self.generate_power_up(score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.shield = True
                player.hammer = True
                player.time = True
                player.has_power_up = True
                player.type = power_up.type
                if player.type == SHIELD_TYPE:
                    player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                elif player.type == HAMMER_TYPE:
                    player.power_up_time = power_up.start_time + (power_up.duration * 1500)
                elif player.type == TIME_TYPE:
                     player.power_up_time = power_up.start_time + (power_up.duration * 500)
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)
