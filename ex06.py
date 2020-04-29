# -- coding: utf-8 --

types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
# 2 strings inside a string
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

# string into a string into a string (2 levels deep)
print(f"I said: {x}")
print(f"I also said: '{y}'.")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# adding string into a string
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# + allows to 'stick' strings together
print(w + e)
