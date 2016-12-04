#!/usr/bin/env python3

def ask():
    """Function to ask for a piece of plaintext and turn its letters into capital letters"""
    plaintext = input("What message would you like to encrypt?")
    plaintext = plaintext.upper()
    return plaintext

def cipher_details():
    """Asks the user whether they are running encryption or decryption"""
    # function will ask until it gets an answer it likes
    while True:
        cryption = input("Are you running (E)ncryption or (D)ecryption?")
        # if the first letter of the input is E, it will encrypt
        if cryption[0] == 'e' or cryption[0] == 'E':
            return 'E'
        # if the first letter of the input is D, then it will decrypt
        elif cryption[0] == 'd' or cryption[0] == 'D':
            return 'D'

def shift_details(crypt_type):
    """Asks user how many letters will be shifted"""
    if crypt_type == 'E':
        while True:
            shift = input("How many letters would you like to shift?")
            # checks if the user inputted an integer
            try:
               int(shift)
            # if not, raises exception and asks again
            except ValueError:
                print("That is not an integer!")
                continue
            return int(shift)
    elif crypt_type == 'D':
        while True:
            shift = input("How many letters were shifted during encryption?")
            # checks if the user inputted an integer
            try:
               int(shift)
            # if not, raises exception and asks again
            except ValueError:
                print("That is not an integer!")
                continue
            return int(shift)

def encrypt(plaintext, key):
    """Runs the encryption by adding the key to each letter of the plaintext"""
    cipherlist = []
    for char in plaintext:
        x = ord(char)
        # if x is a capital letter, it gets encrypted
        if x in range(65,91):
            # turns each letter into a umber 0 - 25
            x -= 65
            # adds the key to the plaintext letter by letter
            x += key
            # loops back to the beginning if the encrypted letter goes beyond Z
            if x > 25:
                x -= 26
            x += 65
            cipherlist.append(chr(x))
        # for non-letters, nothing happens
        else:
            cipherlist.append(char)
    print(''.join(cipherlist))

def decrypt(ciphertext, key):
    """Runs the decryption by subtracting the key from each letter of the ciphertext"""
    cipherlist = []
    for char in ciphertext:
        x = ord(char)
        # if x is a capital letter, it gets encrypted
        if x in range(65,91):
            # turns each letter into a umber 0 - 25
            x -= 65
            # subtracts the key from the plaintext letter by letter
            x -= key
            # loops back to the beginning if the encrypted letter goes beyond Z
            if x > 25:
                x -= 26
            x += 65
            cipherlist.append(chr(x))
        # for non-letters, nothing happens
        else:
            cipherlist.append(char)
    print(''.join(cipherlist))

text = ask()
cryption = cipher_details()
shift = shift_details(cryption)
print(shift)

if cryption == 'E':
    encrypt(text, shift)
elif cryption == 'D':
    decrypt(text, shift)
