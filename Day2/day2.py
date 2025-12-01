def f(mini, maxi):
    count = 0
    while mini < maxi:
        lo = len(str(mini))
        if lo % 2 == 1:
            mini = 10 ** lo
            continue
        base = int(str(mini)[:int(lo/2)])
        if int(str(mini)[int(lo/2):]) > base:
            base += 1
        for i in range(base, 10 ** int(lo / 2)):
            twice = i * 10 ** int(lo / 2) + i
            if twice > maxi:
                break
            count += twice
        mini = 10 ** lo
    return count

def g(mini, maxi):
    count = 0
    found = set()
    lo = len(str(mini))
    n_digit_maxi = len(str(maxi))
    for i in range(1, 10 ** (int(n_digit_maxi / 2))):
        n_digit_i = len(str(i))
        for n in range(max(2, lo // n_digit_i), n_digit_maxi+1):
            twice = int(str(i) * n)
            if twice > maxi:
                break
            if twice < mini or twice in found:
                continue
            found.add(twice)
            count += twice
    return count


count = 0
with open("input.txt") as l:
    for i in l.readline().split(','):
        mini = int(i.split('-')[0])
        maxi = int(i.split('-')[1])
        count += f(mini, maxi)
        
print(count)

count = 0
with open("input.txt") as l:
    for i in l.readline().split(','):
        mini = int(i.split('-')[0])
        maxi = int(i.split('-')[1])
        count += g(mini, maxi)
        
print(count)