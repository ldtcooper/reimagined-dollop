#!/usr/bin/python3

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

def grid_gen(plaintext, key):
    """Creates a list of lists to do the encryption"""
    grid = []
    while True:
        grid.append([])
        if len(grid) * key < len(plaintext):
            continue
        else:
            return grid

def encryption(plaintext, grid, key):
    """Encrypts the plaintext using a grid of a size determined by the grid_gen function"""
    # counter for which sub-list letters will be appended to
    lst =0
    # loop to write plaintext to grid
    for letter in plaintext:
        # puts letters into grid
        grid[lst].append(letter)
        # moves to the next row after all the columns are filled in
        if len(grid[lst]) == key:
            lst += 1
    # empty list for ciphertext to be put into
    cipher_list = []
    # counter for which column the function will draw letters from
    take = 0
    # loop to read plain text from grid as ciphertext
    while len(cipher_list) < len(plaintext):
        # iterates through the columns of the grid
        for elem in grid:
            try:
                cipher_list.append(elem[take])
            # if the function finds a list with too few indices, it will know that it has reached the end of the message
            except IndexError:
                print(''.join(cipher_list))
                break
        take += 1






G = grid_gen("Hello there world", 3)
encryption("Hello there world", G, 3)
