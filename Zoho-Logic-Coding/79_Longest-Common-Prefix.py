lst = list(map(str,input("Enter the words separated by space : ").split()))
result = []
minimum_len = min(lst,key=len)
for i in range(len(minimum_len)):
    temp = minimum_len[i]
    flag = False
    for word in lst:
        if temp in word[i]:
            flag = True
        else:
            flag = False
            break
    if flag:
        result.append(temp)
if len(result) == 0:
    result = '""'
else:
    result = "".join(result)
print(f'Longest Common Prefix of {lst} is {result}')

# Sample Input and Sample Output

# Enter the words separated by space : flower flow flight
# Longest Common Prefix of ['flower', 'flow', 'flight'] is fl

# Enter the words separated by space : interview internet internal
# Longest Common Prefix of ['interview', 'internet', 'internal'] is inter

# Enter the words separated by space : dog racecar car   
# Longest Common Prefix of ['dog', 'racecar', 'car'] is ""