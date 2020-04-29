from sys import argv, exit

filename = argv[1]

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you want that, hit RETURN.")

input("???")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!!!")
# target.truncate()
# 'w' mode truncates the file, so no need for the command above ( CONFIRMED!)
# 'a' adds to the file in a new line, keeping what's in the file already
# 'r' is read only, the target.write command will give an error

print("Now I'm going to ask you for 3 lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1  + "\n" + line2 + "\n" + line3 + "\n")

print("And finally we close it.")
target.close()

exit(0)