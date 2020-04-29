numbers = []

def add_to_list(alist, therange):
    i = 0
    while i < therange:
        print(f"At the top is {i}")
        alist.append(i)

        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom is {i}")

add_to_list(numbers, 5)

print("The numbers: ")
for num in numbers:
    print(num, end=" -> ")

print("\b\b\b\b   ")