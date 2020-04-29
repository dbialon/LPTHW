from sys import argv, exit

script, input_file = argv

## print the whole file f using .read()
## could use this instead
## print open(input_file).read()
## but we want to use the file globally
## not just in this function
def print_all(f):
	print(f.read())
	
## we're using .seek to go back to a line in file
## .seek(offset[, whence])
## offset is the 'distance' from current position 'whence'
## whence is set to 0 as default and can be ommitted
## 0 begining of file
## 1 current position, 2 end of file
def rewind(f):
	f.seek(0)
	
## prints just one line
## .readline reads a line in current position
## and after sets position in the next line
## line_count just counts the lines
## .readline() moves the cursor to the next line
## .strip() removes '\n' at the end of each line
def print_a_line(line_count, f):
	print(line_count, " ---> ", f.readline().strip())

## opens the input file	
current_file = open(input_file, 'r')

print("\nFirst let's print the whole file:\n")

## prints the whole file, now position is at the end of the file
## so we need to rewind to the beginning
print_all(current_file)

print("\nNow let's rewind, kind of like a tape.\n")

## rewind to the beginning, position 0
rewind(current_file)

print("""
Let's print three lines:"
LC --->  .readline()
""", end="")

## we're in 0 position, .readline prints line 1 of current_file
## and sets position in line 2
current_line = 1 ## current line = 1
print_a_line(current_line, current_file)

## here it prints line 2 and goes to line 3
current_line += 1 ## current line = 2
print_a_line(current_line, current_file)

## here it prints line 3 and after it runs
## sets position at the end of the file
## because there are only 3 lines
current_line += 1 ## current line = 3
print_a_line(current_line, current_file)

## close the file
current_file.close()

exit(0)