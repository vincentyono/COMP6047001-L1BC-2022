import pygame
import json
from random import randint


class Vehicle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.__vehicle_sheet = pygame.image.load(
            "assets/vehicles.png").convert_alpha()
        self.type = randint(1, 2)

        with open("assets/vehicles_sprites.json", "r") as f:
            self.data = json.loads(f.read())

        if self.type == 1:
            self.vehicle_surface = pygame.Surface(
                (self.data["frames"]["car1"]["sourceSize"]["w"], self.data["frames"]["car1"]["sourceSize"]["h"]))
            self.vehicle_surface.set_colorkey((0, 0, 0))
            self.vehicle_surface.blit(
                self.__vehicle_sheet, (0, 0), (self.data["frames"]["car1"]["frame"]["x"], self.data["frames"]["car1"]["frame"]["y"], self.data["frames"]["car1"]["frame"]["w"], self.data["frames"]["car1"]["frame"]["h"]))
        else:
            self.vehicle_surface = pygame.Surface(
                (self.data["frames"]["car2"]["sourceSize"]["w"], self.data["frames"]["car2"]["sourceSize"]["h"]))
            self.vehicle_surface.set_colorkey((0, 0, 0))
            self.vehicle_surface.blit(
                self.__vehicle_sheet, (0, 0), (self.data["frames"]["car2"]["frame"]["x"], self.data["frames"]["car2"]["frame"]["y"], self.data["frames"]["car2"]["frame"]["w"], self.data["frames"]["car2"]["frame"]["h"]))

        self.__x = x
        self.__y = y

        self.__speed = 5

    def update(self):
        self.rect = self.vehicle_surface.get_rect()
        self.__x -= self.__speed
        if self.__x < -100:
            self.__x = 900
            self.type = randint(1, 2)

        if self.type == 1:
            self.vehicle_surface = pygame.Surface(
                (self.data["frames"]["car1"]["sourceSize"]["w"], self.data["frames"]["car1"]["sourceSize"]["h"]))
            self.vehicle_surface.set_colorkey((0, 0, 0))
            self.vehicle_surface.blit(
                self.__vehicle_sheet, (0, 0), (self.data["frames"]["car1"]["frame"]["x"], self.data["frames"]["car1"]["frame"]["y"], self.data["frames"]["car1"]["frame"]["w"], self.data["frames"]["car1"]["frame"]["h"]))

        else:
            self.vehicle_surface = pygame.Surface(
                (self.data["frames"]["car2"]["sourceSize"]["w"], self.data["frames"]["car2"]["sourceSize"]["h"]))
            self.vehicle_surface.set_colorkey((0, 0, 0))
            self.vehicle_surface.blit(
                self.__vehicle_sheet, (0, 0), (self.data["frames"]["car2"]["frame"]["x"], self.data["frames"]["car2"]["frame"]["y"], self.data["frames"]["car2"]["frame"]["w"], self.data["frames"]["car2"]["frame"]["h"]))

    def get_position(self):
        return (self.__x, self.__y)

    def get_rect(self):
        return (self.__x, self.__y, self.data["frames"][f"car{self.type}"]["sourceSize"]["w"], self.data["frames"][f"car{self.type}"]["sourceSize"]["h"])
