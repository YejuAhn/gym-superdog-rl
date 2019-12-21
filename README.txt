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
    - 4 Action Spaces (Up, Left, Right, Space)
    - The step function expects an array of 0 and 1 that represents


Initiating the environment:
    - superdog can be initiated with:
        import gym
        env = gym.make('superdog-1-1-tiles-v0')
        env.reset()

Gameplay:
    - The game will automatically close if Superdog dies or shortly after the goal is touched
    - The game will only accept inputs after the timer has started to decrease (i.e. it will automatically move
      through the menus and animations)
    - The total reward is the distance on the x axis.

Variables:
    - The following variables are available in the info dict
      - distance        # Total distance from the start (x-axis)
      - life            # Number of lives Superdog has (3 if Superdog is alive, 0 is Superdog is dead)
      - player_status   # Indicates if Superdog is small (value of 0), big (value of 1), or can shoot bones (2+)
      - ignore          # Will be added with a value of True if the game is stuck and is terminated early












