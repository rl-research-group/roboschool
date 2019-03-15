import roboschool, gym
import numpy as np
from time import sleep
import sys
from agent_zoo.RoboschoolWalker2d_v1_2017jul import ZooPolicyTensorflow
import tensorflow as tf

env_name=sys.argv[1]
print("Using environment {}".format(env_name))
config = tf.ConfigProto(
    inter_op_parallelism_threads=1,
    intra_op_parallelism_threads=1,
    device_count = { "GPU": 0 } )
sess = tf.InteractiveSession(config=config)

env = gym.make('RoboschoolWalker2d-v1')
agent = ZooPolicyTensorflow("Test_gravity1", env.observation_space, env.action_space)

envm = gym.wrappers.Monitor(env, env_name, video_callable=lambda x: True, force=True)
obs0 = envm.reset()
score = 0

print("Before Gravity Change")
done=False
while not done:
    action = agent.act(obs_data=obs0 , cx=None)
    obs1, r, done, _ = envm.step(action)
    obs0=obs1
    score += r
    # envm.render("human")

obs0=envm.reset()
envm.env.env.scene.cpp_world.set_gravity(100000)
print("After Gravity Change")
done=False
while not done:
    action = agent.act(obs_data=obs0 , cx=None)
    obs1, r, done, _ = envm.step(action)
    obs0=obs1
    # envm.render()
