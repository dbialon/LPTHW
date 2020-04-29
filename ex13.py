# -- coding: utf-8 --
from sys import argv, exit

if len(argv) != 4:
    print("Invalid input. Provide 3 variables.")
    exit(1)

script, first, second, third = argv

print(f"The script is called: {script}")
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
exit(0)
