# -- coding: utf-8 --

#import module - argument variable - from sys package
from sys import argv

# assign names to arg variables
filename = argv[1]

# open a file named 'filename' and load it into 'txt' variable
# it creates a file object
txt = open(filename)

print(f"\nHere is your file {filename}:")
# print contents of the txt variable - a file we just opened
# get contents by .read function
print(txt.read())

# request name of a file and assagn it to file_again variable
file_again = input("\nType the filename again: ")

# open a file, get a name from file_again variable
# creates file object named txt_again
txt_again = open(file_again)

# print contents of text again variable#
#get contents by .read function
print(txt_again.read())

txt.close()
txt_again.close()

print("\n\xa9 Dawid Bia\u0142o\u0144 github.com/dbialon")