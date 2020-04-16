# RPS Component 2 - Randomly a generate an action

import random

action = ["Rock", "Paper", "Scissor"]

for item in range(0,20):

    cpu_action = random.choice(action)
    print(cpu_action)
