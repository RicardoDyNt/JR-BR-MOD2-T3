import pygame
import random

from dino_runner.components.obstacles.cactus import CactusSmall, CactusLarge
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import BIRD, HAMMER_TYPE, SHIELD_TYPE, SMALL_CACTUS, LARGE_CACTUS, TIME_TYPE, DEATH_SOND
from pygame import mixer


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0,2) == 0:
                self.obstacles.append((CactusSmall(SMALL_CACTUS)))
            elif random.randint(0,2) == 1:
                self.obstacles.append((CactusLarge(LARGE_CACTUS)))
            elif random.randint(0,2) == 2:
                self.obstacles.append(Bird(BIRD))
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    self.play_music_death()
                    break
                else: 
                    if game.player.type == HAMMER_TYPE:
                        self.obstacles.remove(obstacle)
                    elif game.player.type == TIME_TYPE:
                        rapid_or_slowly = random.randint(0,1)
                        if rapid_or_slowly == 0:
                            game.game_speed += 20
                        else:
                            game.game_speed -= 20
                            self.obstacles.remove(obstacle)      

                       
    def reset_obstacles(self):
        self.obstacles = []     

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)        

    def play_music_death(self):
        pygame.mixer.music.load(DEATH_SOND)
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume == 40