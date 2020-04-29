# -- coding: utf-8 --
from time import sleep

print("\nStop!")
sleep(0.5)

name = input("Who's there? ")
age = input(f"How old are you, {name}? ")
height = input("How tall are you? ")
weight = input("And how much do you weigh? ")

sleep(0.5)
print(f"So {name}, you're {age} years old, {height} tall and {weight} heavy.")
sleep(1)
print(f"You may pass, {name}.")
