#main.py
#Nicholas Norman
#March 2024

import setup

#show simulation variables
print("--------------------------------------")
print("SIMULATION STARTING WITH...")
print("--------------------------------------")
print(f"Intial Population:              {setup.initial_pop}")
print(f"Intial Life Expectancy:         {setup.initial_expec}")
print(f"Intial Mutation Coeff:          {setup.initial_mut}")
print(f"Max years gained from Mutation: {setup.t_max}")
print(f"Number of rounds:               {setup.round_count}")
print(f"Offspring per Pregnancy:        {setup.offspring}")
print(f"Chance of death at birth:       {setup.D.d_born}%")
print(f"Chance of death at max age:     {setup.D.d_death}%")
print(f"Chance of death modeled:        linear")
print("--------------------------------------")