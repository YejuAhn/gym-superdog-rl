from gym.envs.registration import register

register(
    id='world_1',
    entry_point='gym_superdog_rl:World_1',
    max_episode_steps=2000,
)




