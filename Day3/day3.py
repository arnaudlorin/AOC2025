
def find_largest_joltage(line, n):
    maxi = [0] * n
    filled = 0
    for ii, i in enumerate(line):
        for j in range(max(filled, ii - len(line) + n), n):
            if maxi[j] == 9:
                filled += 1
                continue
            if int(i) > maxi[j]:
                maxi[j] = int(i)
                i = 0
                continue
            if i == 0:
                maxi[j] = 0
                continue
    result = ''
    for i in maxi:
        result += str(i)
    return int(result)



count = 0
count12 = 0
with open("input.txt") as f:
    for l in f.readlines():
        count += find_largest_joltage(l.strip('\n'), 2)
        count12 += find_largest_joltage(l.strip('\n'), 12)

print(count, count12)