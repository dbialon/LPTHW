# -- coding: utf-8 --

print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
# word snow is in quotes to make sure it's treated as word, not a variable
print("And everywhere that Mary went.")
print("." * 10) # what'd that do? it prints ..........
# strings can not only be added but also multiplied

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
# a comma at the end of a 'print' line will make the next 'print'
# appear in the same line but adds a 'space'
