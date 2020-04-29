# -- coding: utf-8 --

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4)) # no quotes for numbers
print(formatter.format("one", "two", "three", "four")) # with quotes for words
print(formatter.format(True, False, False, True)) # keywords don't need quotes
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight"
))
# output will be printed out on a single line
# commas are necessary
