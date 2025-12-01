dial_size = 100
dial = 50
password = 0

with open("input.txt") as f:
    for l in f:
        shift = int(l[1:])
        if l[0] == 'L':
            dial = (dial - shift) % dial_size
        elif l[0] == 'R':
            dial = (dial + shift) % dial_size
        else:
            raise Exception("beavior not defined")
        if dial == 0:
            password += 1
            
print(dial)
print(password)