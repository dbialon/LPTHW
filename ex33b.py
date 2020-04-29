numbers = []

def add_to_list(alist, therange, step):
    i = 0
    while i < therange:
        print(f"At the top is {i}")
        alist.append(i)

        i += step
        print("Numbers now: ", numbers)
        print(f"At the bottom is {i}")

add_to_list(numbers, 25, 4)

print("The numbers: ")
for num in numbers:
    print(num, end=" -> ")

print("\b\b\b\b   ")