import roboschool, gym
import numpy as np
from time import sleep
import sys

env_name=sys.argv[1]
print("Using environment {}".format(env_name))
env = gym.make('RoboschoolWalker2d-v1')
envm = gym.wrappers.Monitor(env, env_name, video_callable=lambda x: True, force=True)
envm.reset()

print("Before Gravity Change")
for i in range(100):
    _, _, done, _ = envm.step(envm.action_space.sample())
    if done:
        break
    envm.render()

envm.env.scene.cpp_world.set_gravity(0)
print("After Gravity Change")
for i in range(100):
    _, _, done, _ = envm.step(envm.action_space.sample())
    if done:
        break
    envm.render()
