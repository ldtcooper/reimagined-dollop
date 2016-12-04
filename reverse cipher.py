#!/usr/bin/env python3

plaintext = input("What message would you like to encode?")
plaintext = plaintext.upper()

revlist = []
for letter in plaintext:
    revlist.append(letter)
revlist.reverse()
print(''.join(revlist))
