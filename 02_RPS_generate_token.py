# RPS Component 2 - Randomly a generate an attack

import random

attacks = ["Rock", "Paper", "Scissor"]

for item in range(0,20):

    cpu_attack = random.choice(attacks)
    print(cpu_attack)
