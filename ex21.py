def add(a, b):
	print(f"ADDING {a} + {b}")
	return a + b
	
def subtract(a, b):
	print(f"SUBTRACTING {a} - {b}")
	return a - b
	
def multiply(a, b):
	print(f"MULTIPLYING {a} * {b}")
	return a * b
	
def divide(a, b):
	print(f"DIVIDING {a} / {b}")
	return a / b
	

print("\nLet's do some math with just functions!\n")

age = add(30, 5)         ##35
height = subtract(78, 4) ##74
weight = multiply(90, 2) ##180
iq = divide(100, 2)      ##50

print(f"\nAge: {age}, Height: {height}, Weight: {weight}, IQ: {iq}\n")


## A puzzle for the extra credit, type it in anyway.
print("Here is the puzzle.\n")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("\nThat becomes: ", what, "\nCan you do it by hand?\n")