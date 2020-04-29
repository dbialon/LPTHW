# -- coding: utf-8 --

from sys import argv

script, user_name, age = argv
prompt = 'Answer: '

print(f"\nHi {user_name}, I'm {script} script.")
print("I'd like to ask you a few questions.")
print(f"Question: Do you like me, {user_name}?")
likes = input(prompt)

print(f"Where do you live, {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("What is your occupation?")
job = input(prompt)

print(f"""
Alright, so you said '{likes}' about liking me.
You are {age} years old and live in {lives}. Not sure where that is.
You work as a {job}.
And you have a {computer} computer. Nice.
""")

print("\xa9 Dawid Bia\u0142o\u0144 github.com/dbialon")
