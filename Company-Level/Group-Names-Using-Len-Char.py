# Question : Given a list of names (as strings), write a Python program to group the names by their lengths?

names = list(map(str,input("Enter the names separated by space : ").split()))
result = {}
for name in names:
    name_len = len(name)
    if name_len not in result:
        result[name_len] = [name]
    else:
        result[name_len].append(name)
for i in result:
    print(f'Names with {i} Characters -> {result[i]}')

# Sample Output : 
# Enter the names separated by space : vijay swathi deeksha raman subu joe
# Names with 5 Characters -> ['vijay', 'raman']
# Names with 6 Characters -> ['swathi']
# Names with 7 Characters -> ['deeksha']
# Names with 4 Characters -> ['subu']
# Names with 3 Characters -> ['joe']