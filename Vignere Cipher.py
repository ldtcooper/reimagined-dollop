#!/usr/bin/python3

# Programmed for my Introduction to Python course at UC Santa Cruz in Fall 2016


# Returns a variable (str) given a prompt
def prompt(question):
    user_input = str(input(question))
    user_input = user_input.upper()
    user_input = user_input.strip()
    return user_input


# checked encryption method against that found here: http://stackoverflow.com/questions/26752933/python-vigenere-cipher-going-further-than-needed
# noinspection PyShadowingNames
def encryption(plaintext, key):
    # ord("A")==65
    # creates empty string that the enciphered text can be added on to
    enciphered = ""
    # adds values of key letters to those of the plaintext
    for char in range(len(plaintext)):
        # skips spaces for encryption
        if plaintext[char] == " ":
            continue
        # the encryption happens in the following steps
        cipherletter = (ord(plaintext[char]) - 65) + ((ord(key[char])) - 65)
        # loops encryption around the alphabet
        if cipherletter > 25:
            cipherletter -= 26
        enciphered += chr(cipherletter + 65)
    # Found method for splitting up strings into blocks here: http://stackoverflow.com/questions/3258573/pythonic-way-to-insert-every-2-elements-in-a-string
    enciphered = ' '.join(enciphered[i:i + 8] for i in range(0, len(key), 8))
    print("Your encrypted message is: ", enciphered)


# modified from encryption function above
# noinspection PyShadowingNames
def decryption(ciphertext, key, x):
    # ord("A")==65
    # creates empty string that the enciphered text can be added on to
    deciphered = ""
    # skips deciphering non-letters
    for char in range(len(ciphertext)):
        if ord(ciphertext[char]) < 65 or ord(ciphertext[char]) > 90:
            cipherletter = ciphertext[char]
            deciphered += cipherletter
        else:
            # subtracts value of key letter from the ciphertext letter
            cipherletter = (ord(ciphertext[char]) - 65) - (ord(key[x]) - 65)
            # loops around for negative numbers
            if cipherletter < 0:
                cipherletter += 26
            deciphered += chr(cipherletter + 65)
            # moves they key along
            x += 1
            # resets the key when it reaches the end
            if x == len(key):
                x = 0
    print(deciphered)


# keeps asking for encryption or decryption until the program gets an input starting with "E" or "D"
while True:
    cryption = prompt("Would you like to (E)ncrypt or (D)ecrypt?")
    if cryption[0] == "E":
        cryption = "encrypt"
        break
    elif cryption[0] == "D":
        cryption = "decrypt"
        break

# assigns values for message and key
orig_text = prompt("What is your message?")
key = prompt("What is the key?")

# runs encryption or decryption functions based on which the user requested
# noinspection PyUnboundLocalVariable
if cryption == "encrypt":
    # Found this method for removing non-letters at http://stackoverflow.com/questions/3939361/remove-specific-characters-from-a-string-in-python
    for letter in orig_text:
        if ord(letter) < 65 or ord(letter) > 90:
            orig_text = orig_text.replace(letter, "")
    # repeats the key in its entirety as many times as it can and still be shorter than the plaintext
    key = (key * (len(orig_text) // len(key)))
    # if there is still leftover space, this adds part of the key to the existing key until the repeated key is as long as the plaintext
    if len(key) != len(orig_text):
        key = key + key[:(len(orig_text) % len(key))]
    else:
        pass
    # run encryption function
    encryption(orig_text, key)
elif cryption == "decrypt":
    # repeats the key in its entirety as many times as it can and still be shorter than the plaintext
    decryption(orig_text, key, 0)
