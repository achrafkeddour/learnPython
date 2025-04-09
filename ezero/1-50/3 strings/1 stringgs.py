# ---------------------
# -- Strings Methods --
# ---------------------


# strip() – Removes whitespace (or specified characters) from both ends of a string.
# rstrip() – Removes whitespace (or specified characters) from the right end of a string.
# lstrip() – Removes whitespace (or specified characters) from the left end of a string.

a = "    achraf    " ; b ="@@@achraf@@@"
print(a.strip()) # achraf

print(b.strip("@")) # achraf
print(b.rstrip("@")) # @@@achraf
print(b.lstrip("@")) # achraf@@@


# title() – Converts the first character of each word to uppercase and the rest to lowercase.
c = "I Love 2d Graphics and 5g Technology and python"
print(c.title()) # I Love 2D Graphics And 5G Technology And Python


# zfill(number) – Pads the string on the left with zeros to reach the specified length
one = "1" ; two = "22" ; four = "4444"
print(one.zfill(4)) # 0001
print(two.zfill(4)) # 0022
print(four.zfill(4)) # 4444
