import math
dial_size = 100
dial = 50
password = 0

with open("input.txt") as f:
    for l in f:
        shift = int(l[1:])
        password += math.floor(shift / dial_size)
        shift = shift % 100
        if l[0] == 'L':
            if dial - shift < 0 and dial != 0:
                password += 1
            dial = (dial - shift) % dial_size
        elif l[0] == 'R':
            if dial + shift > dial_size:
                password += 1
            dial = (dial + shift) % dial_size
        else:
            raise Exception("beavior not defined")
        if dial == 0:
            password += 1
        print(dial, password)
            
print(dial)
print(password)