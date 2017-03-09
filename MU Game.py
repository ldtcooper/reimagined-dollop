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


# function to derive theorems based on the above rules
def derivation(theorem_dict, count):
    # dictionary to keep track of new theorems
    new_theorem_dict = {}
    # iterates through the dictionary of theorems and applies rules
    for elem in theorem_dict:
        # condition for rule 1
        if elem[-1] == 'I':
            theorem = I(elem)
            new_theorem_dict[theorem] = theorem_dict[elem] + '1'
        # rule 2 can always run
        theorem = II(elem)
        new_theorem_dict[theorem] = theorem_dict[elem] + '2'
        # condition for rule 3
        if 'III' in elem:
            # warning, this time theorem is a list!
            theorem = III(elem)
            # iterates through each possible theorem produced by rule 3
            for string in theorem:
                new_theorem_dict[string] = theorem_dict[elem] + '3'
        # condition for rule 4
        if 'UU' in elem:
            # warning, this time theorem is a list!
            theorem = IV(elem)
            for string in theorem:
                new_theorem_dict[string] = theorem_dict[elem] + '4'
    if 'MU' in new_theorem_dict:
        print("Sucess after {0} rounds! Theorem 'MU' derived with the steps {1}".format(count, new_theorem_dict['MU']))
    else:
        print("No 'MU' in round {0} - Trying again".format(count))
        derivation(new_theorem_dict, count+1)

# given 'MI', prove 'MU'
derivation({'MI':'G'}, 1)


