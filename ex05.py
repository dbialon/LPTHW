# -- coding: utf-8 --

name = 'Dawid S. Bialon'
age = 40
height = 178 #in cms
weight = 108 #in kgs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {age} years old.")
print(f"He's {height / 100} meters tall. That's {height * 0.393701} inches") # 1cm = 0.393701in
print(f"He's {weight} kilograms heavy. That's {weight * 0.2020462} lbs.") # 1kg = 2.20462lbs
print("Actually it's a bit heavy.")
print(f"He's got {eyes.lower()} eyes and {hair.lower()} hair.")
print(f"He's teeth are usually {teeth.lower()} depending on the coffee.")
print(f"If I add {age}, {height} and {weight} I get {age + height + weight}.")