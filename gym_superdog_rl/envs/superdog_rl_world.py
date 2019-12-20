import pygame
import random
import numpy as np
import os

class WorldView:
    def __init__(self, world_size = (30, 30), screen_size = (500, 500)):
        #pygame configurations
        pygame.init()
        pygame.display.set_caption("Adventure of Superdog")
        self.clock = pygame.time.Clock()
        self.__game_over = False
        self.__world = World(world_size = world_size)
        self.world_size = self.__world.world_size
        self.screen = pygame.display.set_mode(screen_size)
        #starting point
        self.__entrance = np.zeros(2, dtype=int)

        #set goal
        self.__goal = np.array(self.world_size) - np.array((1, 1))

        #agent 
        self.__dog = self.__entrance

        #background
        self.background = pygame.transform.scale(pygame.image.load('/Users/jessicaahn/Desktop/bg_grasslands.png'), screen_size)

        # show world
        self.__draw_world()

        # # show dog
        # self.__draw_dog()

        # # show entrance
        # self.__draw_entrance()

        # # show end goal
        # self.__draw_goal()


    def update(self, mode="human"):
        try:
            img_output = self.view_update(mode)
            self.update_controller()
        except Exception as e:
            self.__game_over = True
            self.quit_game()
            raise e
        else:
            return img_output

    def quit_game(self):
        try:
            self.__game_over = True
            if self.__enable_render is True:
                pygame.display.quit()
            pygame.quit()
        except Exception:
            pass


    def move_dog(self, dir):
        if dir not in self.__world.COMPASS.keys():
            raise ValueError("dir cannot be %s. The only valid dirs are %s."
                             % (str(dir), str(self.__world.COMPASS.keys())))

        if self.__world.is_open(self.__dog, dir):
            # update the drawing
            self.__draw_dog(transparency=0)
            # move the dog
            self.__dog += np.array(self.__dog.COMPASS[dir])
            # if in portal after the move
            if self.maze.is_portal(self.robot):
                self.__dog = np.array(self.maze.get_portal(tuple(self.dog)).teleport(tuple(self.dog)))
            self.__draw_dog(transparency=255)


    def reset_dog(self):
        self.__draw_dog(transparency=0)
        self.__dog = np.zeros(2, dtype=int)
        self.__draw_dog(transparency=255)


    def update_controller(self):
        if not self.__game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__game_over = True
                    self.quit_game()


    def view_update(self, mode="human"):
        if not self.__game_over:
            # update the robot's position
            # self.__draw_entrance()
            # self.__draw_goal()
            # self.__draw_dog()

            # update the screen
            self.screen.blit(self.background, (0, 0))

            if mode == "human":
                pygame.display.flip()

            return np.flipud(np.rot90(pygame.surfarray.array3d(pygame.display.get_surface())))


    def __draw_world(self):
        #draw blocks
        pass

class World: #Tile Representation

    def __init__(self, world_size =  (30, 30)):
        self.world_size = world_size







if __name__ == "__main__":
    world = WorldView(world_size = (30, 30), screen_size = (500, 500))
    world.update()

    input("Enter any key to quit.")