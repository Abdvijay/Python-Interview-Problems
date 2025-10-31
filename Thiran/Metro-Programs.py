green_line = ['A','B','C','D','E','F','G','H']
red_line = ['I','C','J','K','L','D','E','M','G','N']

junction_point = list(set(green_line) & set(red_line))
print(f'1. Junction point of Green line and Red line is {sorted(junction_point)}')

result = []
for i in green_line:
    if i in junction_point:
        result.append(i)
    if i == 'E':
        break
print(f'2. Number of junctions crossed is {len(result)} which is {result}')