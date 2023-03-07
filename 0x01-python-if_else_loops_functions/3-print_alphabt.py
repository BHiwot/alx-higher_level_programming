#!/usr/bin/python3
for b in range(ord('a'), ord('z') + 1):
    letter = chr(b)
    if letter not in "qe":
    print("{:c}".format(letter), end="")
