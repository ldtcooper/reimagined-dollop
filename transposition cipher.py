#!/usr/bin/python3

import numpy as np

# modified from caesar shift program
def ask():
    """Function to ask for a piece of plaintext, turn its letters into capital letters, and remove spaces"""
    plaintext = input("What message would you like to encrypt?")
    plaintext = plaintext.upper().replace(" ", "")
    return plaintext

# taken from caesar shift program
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

def keymaker (text_length):
    """Asks the user for a key to en/decrypt the text"""
    while True:
        try:
            key = int(input("What numerical key would you like to use? (Integers shorter than the message only)"))
        # asks for a new key if the inputted key is not an integer
        except:
            print("That was not a valid key. Please enter an integer.")
            continue
        # asks for a new key if the inputted key is too long
        if key > text_length:
            print("That was not a valid key. Please enter an integer larger than the length of the text.")
            continue
        return key

def rowgen (plaintext, key):
    """To determine how many rows a grid needs to encrypt the full message"""
    rows = 1
    # loop to determine number of columns
    while key * rows < len(plaintext):
        rows += 1
    return rows



# array size format: (rows, columns)
def encrypt(plaintext, key, row):
    np.zeroes(1, key)

