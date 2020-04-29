# -- coding: utf-8 --

file = input("\nType the name of a file to be printed > ")

txt = open(file)

print()
print(txt.read(), "\n")

txt.close()
