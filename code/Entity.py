from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

import pygame.image


class Entity:

    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./graphics/' + name).convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self, ):
        pass
