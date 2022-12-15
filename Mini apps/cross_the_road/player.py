import pygame
import json


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.__character_sheet = pygame.image.load(
            "assets/character_sheet.png").convert_alpha()

        self.character_surface = pygame.Surface((24, 24))
        self.character_surface.set_colorkey((0, 0, 0))
        self.character_surface.blit(
            self.__character_sheet, (0, 0), (1032, 0, 24, 24))

        self.__x = 400
        self.__y = 460

        self.sprite_number = 1
        self.__status = "walkup"
        self.__alive = True

        self.animation = {
            "walkup": [f"walkup{i + 1}" for i in range(4)],
            "walkdown": [f"walkdown{i + 1}" for i in range(4)],
            "walkleft": [f"walkleft{i + 1}" for i in range(4)],
            "walkright": [f"walkright{i + 1}" for i in range(4)],
            "runup": [f"runup{i + 1}" for i in range(6)],
            "rundown": [f"rundown{i + 1}" for i in range(6)],
            "runleft": [f"runleft{i + 1}" for i in range(6)],
            "runright": [f"runright{i + 1}" for i in range(6)],
            "die": [f"die{i + 1}" for i in range(4)],
        }

        with open("assets/character_sprites.json", "r") as f:
            self.data = json.loads(f.read())

    def get_input(self):

        RUNNING_SPEED = 2
        WALKING_SPEED = 1

        keys = pygame.key.get_pressed()

        if self.__alive:
            if keys[pygame.K_LSHIFT] and (keys[pygame.K_UP] or keys[pygame.K_w]):
                self.__status = "runup"
                self.sprite_number += 0.5
                self.__y -= RUNNING_SPEED
            if keys[pygame.K_LSHIFT] and (keys[pygame.K_DOWN] or keys[pygame.K_s]):
                self.__status = "rundown"
                self.sprite_number += 0.5
                self.__y += RUNNING_SPEED
            if keys[pygame.K_LSHIFT] and (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
                self.__status = "runright"
                self.sprite_number += 0.5
                self.__x += RUNNING_SPEED
            if keys[pygame.K_LSHIFT] and (keys[pygame.K_LEFT] or keys[pygame.K_a]):
                self.__status = "runleft"
                self.sprite_number += 0.5
                self.__x -= RUNNING_SPEED

            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.__status = "walkup"
                self.sprite_number += 0.5
                self.__y -= WALKING_SPEED
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.__status = "walkdown"
                self.sprite_number += 0.5
                self.__y += WALKING_SPEED
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.__status = "walkright"
                self.sprite_number += 0.5
                self.__x += WALKING_SPEED
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.__status = "walkleft"
                self.sprite_number += 0.5
                self.__x -= WALKING_SPEED

    def get_position(self):
        return self.__x, self.__y

    def change_animation(self, key):
        self.character_surface.fill(pygame.Color(0, 0, 0, 0))
        self.character_surface.blit(self.__character_sheet, (0, 0), (
            self.data["frames"][key]["frame"]["x"], self.data["frames"][key]["frame"]["y"], self.data["frames"][key]["frame"]["w"], self.data["frames"][key]["frame"]["h"]))

    def update(self, vehicles):
        if self.__status == "die":
            self.sprite_number += 0.25

        if self.__status == "die" and self.sprite_number > 3:
            self.sprite_number = 3

        n = int((self.sprite_number % 4) + 1) if self.__status.find(
            "run") == -1 else int((self.sprite_number % 6) + 1)
        self.change_animation(self.__status + str(n))

        self.check_collision(vehicles)

    def check_collision(self, vehicles):
        if pygame.Rect(self.get_position()[0], self.get_position()[1], 24, 24).collidelist([vehicle.get_rect() for vehicle in vehicles]) != -1:
            self.__status = "die"
            self.__alive = False
