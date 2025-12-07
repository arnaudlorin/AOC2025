
file = "input.txt"


with open(file) as f:
    l = f.readline()
    n = len(l)
    i = l.find('S')
    beams_col= [[i, 1]]
    n_split = 0
    for l in f:
        for i, b in enumerate(l):
            if b == '^':
                for beam, n_paths in beams_col:
                    if beam == i:
                        n_split += 1
                        beams_col.remove([beam, n_paths])
                        find_left = False
                        find_right = False
                        for j in range(len(beams_col)):
                            if beams_col[j][0] == beam - 1:
                                beams_col[j][1] += n_paths
                                find_left = True
                            if beams_col[j][0] == beam + 1:
                                beams_col[j][1] += n_paths
                                find_right = True
                        
                        if not find_left and beam > 0:
                            beams_col.append([beam - 1, n_paths])
                        if not find_right and beam < n - 1:
                            beams_col.append([beam + 1, n_paths])
                        

print(f"First star: {n_split}")
total_paths = 0
for _, n_paths in beams_col:
    total_paths += n_paths
print(f"Second star: {total_paths}")