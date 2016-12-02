def spoopy(spoop,is_spoop):
    print(spoop,'spoopy',2*spoop,'me')
    print("spoopy enuf? y/n")
    is_spoop=input()
    if is_spoop=='y':
        print(spoop,"spoopy",2*spoop,"u!")
    elif is_spoop=='n':
        spoop=spoop*2
        spoopy(spoop, is_spoop)
    else:
        print("was spoopy enuf? y/n")
        is_spoop=input()
        spoopy(spoop, is_spoop)

print("Python: U gotta type your responses in quotes!")
print("me: y tho?")
print("Python: u gotta!")
spoopy(2,0)
