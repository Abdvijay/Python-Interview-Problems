lst = list(map(str,input("Enter the words list elements : ").split()))
freq = {}
for word in lst:
    if word not in freq:
        freq[word] = 1
    else:
        freq[word] += 1
result = dict(sorted(freq.items(),key=lambda item:item[1],reverse=True))
for key,value in result.items():
    print(key,value)