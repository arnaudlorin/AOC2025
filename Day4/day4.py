neig = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

def find_access(lattice):
    access = 0
    for i in range(len(lattice)):
        for j in range(len(lattice[0])):
            if lattice[i][j] == '@':
                n_neighbors = 0
                for (ni, nj) in neig:
                    if i + ni == len(lattice) or i + ni == -1 or j + nj == len(lattice[0]) or j + nj == -1:
                        continue
                    if lattice[i + ni][j + nj] == '@':
                        n_neighbors += 1
                if n_neighbors < 4:
                    access += 1
    return access

def find_access_and_remove(lattice):
    access = 0
    for i in range(len(lattice)):
        for j in range(len(lattice[0])):
            if lattice[i][j] == '@':
                n_neighbors = 0
                for (ni, nj) in neig:
                    if i + ni == len(lattice) or i + ni == -1 or j + nj == len(lattice[0]) or j + nj == -1:
                        continue
                    if lattice[i + ni][j + nj] == '@':
                        n_neighbors += 1
                if n_neighbors < 4:
                    access += 1
                    lattice[i][j] = '.'
    return access

count = 0
with open("input.txt") as f:
    lattice = []
    for l in f:
        lattice.append(list(l.strip('\n')))
    print(find_access(lattice))
    while True:
        accessible = find_access_and_remove(lattice)
        count += accessible
        if accessible == 0:
            break
print(count)