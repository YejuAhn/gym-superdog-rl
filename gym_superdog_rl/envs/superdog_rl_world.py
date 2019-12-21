import pygame
import random
import numpy as np
import os


#WorldView class
class WorldView: 
    def __init__(self, world_name = "Adventure of Superdog", tile_size = (16, 13), screen_size = (800, 650), enable_render = True): #width x height
        #pygame configurations
        pygame.init()
        pygame.display.set_caption(world_name)
        self.clock = pygame.time.Clock()

        #superdog initialization
        self.__game_over = False
        self.__mode = 'human' #'algo' or 'human'
        self.screen_size = screen_size
        self.__world = World(tile_size = tile_size, screen_size = screen_size)

        #tile representation
        self.tile_height = 13 
        self.tile_width = 16
        self.tiles = np.zeros(shape=(self.tile_height, self.tile_width), dtype=np.uint8)
        self.tile_size = tile_size

        #initialize window
        self.screen = pygame.display.set_mode(screen_size) 
        self.background = pygame.transform.scale(pygame.image.load('/Users/jessicaahn/Desktop/bg_grasslands.png'), screen_size)



        # #starting point
        # self.__entrance = np.zeros(2, dtype=int)

        # #agent 
        # self.__dog = self.__entrance

        
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


    def view_update(self, mode= "human"):
        if not self.__game_over:
            # update the robot's position
            # self.__draw_entrance()
            # self.__draw_goal()
            # self.__draw_dog()

            # update the screen
            self.screen.blit(self.background, (0, 0))

            if mode == "human":
                pygame.display.flip()

            return np.flipud(np.rot90(pygame.surfarray.array3d(pygame.display.get_surface()))) #REVISIT 


    def __draw_world(self):
        #draw blocks
        pass

class World: #Tile Representation
    def __init__(self, tile_size = (16, 13), screen_size = (800, 650)):
        self.tile_size = tile_size
        self.screen_size = screen_size
        self._generate_world()

    def _generate_world(self): 
        pass #TODO 
        #create boxes 











if __name__ == "__main__":
    world = WorldView()
    world.update()

    input("Enter any key to quit.")