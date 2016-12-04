#!/usr/bin/env python3

def ask():
    """Function to ask for a piece of plaintext and turn its letters into capital letters"""
    plaintext = input("What message would you like to encrypt?")
    plaintext = plaintext.upper()
    return plaintext

