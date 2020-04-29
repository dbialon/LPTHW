# -- coding: utf-8 --

i_m = "I\'m"
tabby_cat = f'\t{i_m} tabbed in.'
persian_cat = 'I\'m split\non a line.'
backslash_cat = 'I\'m \\ a \\ cat.'

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

print("""
    \u0104 ---> \\u0104
    \u0105 ---> \\u0105
    \u0106 ---> \\u0106
    \u0107 ---> \\u0107
    \u0118 ---> \\u0118
    \u0119 ---> \\u0119
    \u0141 ---> \\u0141
    \u0142 ---> \\u0142
    \u0143 ---> \\u0143
    \u0144 ---> \\u0144
    \u00D3 ---> \\u00D3
    \u00F3 ---> \\u00F3
    \u015A ---> \\u015A
    \u015B ---> \\u015B
    \u0179 ---> \\u0179
    \u017A ---> \\u017A
    \u017B ---> \\u017B
    \u017C ---> \\u017C
    """)

print("Dawid Bia\u0142o\u0144")
print("\x0E \x0F \x0B")
print("\x03 \x04 \x05 \x06")
