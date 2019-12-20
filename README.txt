Environments:
    - There are 7 environments available, with the following syntax:
        superdog_rl-<world_number>-tiles-v0
        - world_number is a number between 1 and 8

Tiles:
      - Environment with "Tiles" in their name will return a 16x13 array
      representation of the screen, where each square can have one of
      the following values:

      - 0: empty space
      - 1: object (e.g. platform, items, etc.)
      - 2: enemy
      - 3: superdog


Actions:
    - The NES controller is composed of 6 buttons (Up, Left, Down, Right, A, B)
    - The step function expects an array of 0 and 1 that represents


Initiating the environment:
    - superdog can be initiated with:

        import gym
        env = gym.make('superdog-1-1-tiles-v0')
        env.reset()








