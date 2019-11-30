import pygame
import random
import numpy as np
import os

class World:
    def __init__(self, world_size = (30, 30), screen_size = (500, 500), num_portals = 0, enable_render = True):
        #pygame configurations
        pygame.init()
        pygame.display.set_caption("Adventure of Superdog")
        self.clock = pygame.time.Clock()
        self.__game_over = False
        self.__enable_render = enable_render
        self.__world = World(world_size = world_size, num_portals = num_portals)
        self.world_size = self.__world.world_size


        


if __name__ == "__main__":
    world = World(world_size = (30, 30), screen_size= (500, 500))
    world.update()

    input("Enter any key to quit.")