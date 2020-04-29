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
	
print("""

This programm will execute the following calculation:

(A - B) / C * D + E

""")

varA = float(input("What is your A? --- "))
varB = float(input("What is your B? --- "))
varC = float(input("What is your C? --- "))
varD = float(input("What is your D? --- "))
varE = float(input("What is your E? --- "))

print()
	
result = add(multiply(divide(subtract(varA, varB), varC), varD), varE)

print("\nThat becomes:", result)