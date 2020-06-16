
from random import random, choice
from time import time

# Two dice simulation
start_time = time()

counts = {"Y": 0, "T": 0}


def one_toss_probability():
    p = random()
    if p > 0.50:
        return "T"
    else:
        return "Y"


for i in range(1000):
    t = one_toss_probability()  # "Y" or "T"
    counts[t] += 1
print(counts)  # {'Y': 517, 'T': 483}, differs at each run
print(f"--- AAA {time() - start_time} seconds ---")


start_time = time()
b = [i for i in [[random() > 0.5] for w in range(1000)]]
print("Yazi:", b.count([True]), "Tura:", b.count([False]))
print(f"--- BBB {time() - start_time} seconds ---")


start_time = time()
list = [choice(["heads", "tails"]) for i in range(1000)]
print(f'{list.count("heads")} yazı geldi\n{list.count("tails")} tura geldi')
print(f"--- CCC {time() - start_time} seconds ---")
