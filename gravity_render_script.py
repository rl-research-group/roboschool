import roboschool, gym
import numpy as np
from time import sleep
import sys

env_name=sys.argv[1]
print("Using environment {}".format(env_name))
env = gym.make('RoboschoolWalker2d-v1')
envm = gym.wrappers.Moniter(env, env_name, video_callable=lambda x: True, force=True)
env.reset()

print("Before Gravity Change")
for i in range(100):
    env.step(env.action_space.sample())
    # sleep(0.1)
    env.render()

env.env.scene.cpp_world.set_gravity(0)
print("After Gravity Change")
for i in range(100):
    env.step(env.action_space.sample())
    # sleep(0.1)
    env.render()
