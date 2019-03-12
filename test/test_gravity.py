import roboschool, gym
import numpy as np
from time import sleep
import sys
from agent_zoo.RoboschoolWalker2d_v1_2017jul import ZooPolicyTensorflow

env_name=sys.argv[1]
print("Using environment {}".format(env_name))
env = gym.make('RoboschoolWalker2d-v1')
agent = ZooPolicyTensorflow("Test_gravity1", env.observation_space, env.action_space)

envm = gym.wrappers.Monitor(env, env_name, video_callable=lambda x: True, force=True)
obs0 = envm.reset()
score = 0

print("Before Gravity Change")
for i in range(100):
    agent.act(obs_data=obs0 , cx=None)
    obs1, r, done, _ = envm.step(action)
    score += r
    if done:
        break
    sleep(0.1)
    envm.render("human")

envm.reset()
envm.env.env.scene.cpp_world.set_gravity(1.0)
print("After Gravity Change")
for i in range(100):
    _, _, done, _ = envm.step(envm.action_space.sample())
    if done:
        break
    sleep(0.1)
    envm.render()
