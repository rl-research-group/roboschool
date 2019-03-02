import roboschool, gym
import numpy as np
from time import sleep

env = gym.make('RoboschoolWalker2d-v1')
env.reset()
print("Before Gravity Change")
for i in range(100):
    env.step(env.action_space.sample())
    sleep(0.1)
    env.render()

env.env.scene.cpp_world.set_gravity(0)
print("After Gravity Change")
for i in range(100):
    env.step(env.action_space.sample())
    sleep(0.1)
    env.render()
