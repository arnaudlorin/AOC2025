def make_column_add_calc(column):
    result = 0
    for data in column:
            result += data
    return result

def make_column_mult_calc(column):
    result = 1
    for data in column:
            result *= data
    return result


file = "input.txt"
n = len(open(file).readline().split())
columns = [[] for _ in range(n)]
with open(file) as f:
    for l in f:
        l_split = l.split()
        if l_split[0] in ['+', '*']:
            break
        for i , number in enumerate(l_split):
            columns[i].append(int(number))
            
result = 0
for i, op in enumerate(l_split):
    if op == '+':
        result += make_column_add_calc(columns[i])
    else:
        result += make_column_mult_calc(columns[i])

print(f"First star: {result}")
text = []
with open(file) as f:
    for l in f:
        text.append(l.strip('\n'))
n_row = len(text)
n_cols = len(text[0])
       
data = []
result = 0
for i in range(n_cols -1, -1, -1):
    integer = ""
    for j in range(n_row):
        if text[j][i] in ['', '+', '*']:
            break
        elif text[j][i] == ' ':
            continue
        integer += text[j][i]
    if integer == '':
        if text[-1][i+1] == '+':
            result += make_column_add_calc(data)
        else:
            result += make_column_mult_calc(data)     
    else:
        data.append(int(integer))
        continue
    data = []
    
if text[-1][1] == '+':
    result += make_column_add_calc(data)
else:
    result += make_column_mult_calc(data)     
print(f"Second star: {result}")