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
            return shift
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
            return shift

print(shift_details('D'))
