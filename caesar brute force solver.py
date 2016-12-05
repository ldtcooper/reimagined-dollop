#!/usr/bin/env python3

ciphertext = input("What message would you like to brute force?")
ciphertext = ciphertext.upper()

# initial key to try
try_key = 1

# runs decryption for each of the possible keys
while try_key < 26:
    # sets up empty list for letters
    decrypt_list = []
    for letter in ciphertext:
        # deciphers capital letters
        if ord(letter) in range(65, 91):
            # turns letters into numbers 0-25
            x = ord(letter) - 65
            x -= try_key
            # loops back around if x becomes negative
            if x < 0:
                x += 26
            # turns numbers back into (potentially) deciphered letters
            x = chr(x + 65)
            decrypt_list.append(x)
        # ignores all other characters
        else:
            decrypt_list.append(letter)
    print('{0}:'.format(try_key), ''.join(decrypt_list))
    try_key += 1
    continue




