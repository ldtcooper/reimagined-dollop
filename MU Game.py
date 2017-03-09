#!/usr/bin/env python3

# This is a program inspired by the MU-puzzle found in chapter one of Douglas Hofstadter's "Gödel Escher Bach"

# Defines the effects of each rule - conditions will be added later
# Rule One: Adds 'U' to the end of the string
def I(string):
    string += 'U'
    return string

# Rule 2: Adds x to the end of 'Mx'
def II(string):
    new_string =  string.replace('M', '')
    string += new_string
    return string

# Rule 3: Changes 'III' to 'U'
def III(string):
    #creates list for each possible new string to be entered into
    finish_list = []
    # iterates through string to find each 'III'
    for elem in range(len(string)):
        try:
            if string[elem] == 'I' and string[elem + 1] == 'I' and string[elem + 2] == 'I':
                new_string = string[:elem] + 'U' + string[elem+3:]
                finish_list.append(new_string)
        except:
            continue
    return finish_list

# Rule 4: Drops 'UU' from string
def IV(string):
    # creates list for each possible string
    finish_list = []
    # iterates through string to find each 'UU'
    for elem in range(len(string)):
        try:
            if string[elem] == 'U' and string[elem+1] == 'U':
                new_string = string[:elem] + string[elem+2:]
                finish_list.append(new_string)
        except:
            continue
    return finish_list



