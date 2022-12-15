import pygame
from sys import exit
from player import Player
from vehicle import Vehicle
from random import randint


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 480))
        self.icon = pygame.image.load("assets/logo.png")
        pygame.display.set_caption("Cross the road")
        pygame.display.set_icon(self.icon)

        self.background_image = pygame.image.load("assets/map.png")
        self.clock = pygame.time.Clock()

        self.player = Player()
        self.vehicles = [Vehicle(randint(900, 1200), 64), Vehicle(randint(900, 1200), 96),
                         Vehicle(randint(900, 1200), 128), Vehicle(
                             randint(900, 1200), 160),
                         Vehicle(randint(900, 1200), 288), Vehicle(
                             randint(900, 1200), 320),
                         Vehicle(randint(900, 1200), 352), Vehicle(randint(900, 1200), 384)]

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                self.player.get_input()

            self.blit()
            self.player.update(self.vehicles)
            self.vehicles_update()
            pygame.display.update()
            self.clock.tick(30)

    def blit(self):
        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(self.player.character_surface,
                         self.player.get_position())
        for vehicle in self.vehicles:
            self.screen.blit(vehicle.vehicle_surface,
                             vehicle.get_position())

    def vehicles_update(self):
        for vehicle in self.vehicles:
            vehicle.update()
