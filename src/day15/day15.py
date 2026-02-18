# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 09:52:05 2026

@author: Sharath Kumar
"""

import random
random.seed(2)

actions = ["Click", "Scroll", "Exit"]

# Generate sample space for two consecutive actions
sample_space = [(a1, a2) for a1 in actions for a2 in actions]

print("Sample Space:")
print(sample_space)
print("Total outcomes:", len(sample_space))


# Probability of Event E


event_E = [outcome for outcome in sample_space if "Click" in outcome]

print("\nEvent E (At least one Click):")
print(event_E)

probability_E = len(event_E) / len(sample_space)
print("Theoretical Probability of at least one Click:", probability_E)


# Dice Simulation


trials = 1000
count_sum_7 = 0

for _ in range(trials):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    if die1 + die2 == 7:
        count_sum_7 += 1

experimental_probability = count_sum_7 / trials

print("\nExperimental Probability of Sum = 7 (1000 rolls):")
print(experimental_probability)




