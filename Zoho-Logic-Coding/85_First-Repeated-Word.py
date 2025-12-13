sentence = list(map(str,input("Enter the sentence : ").split()))
result = []
for i in range(len(sentence)):
    flag = False
    for j in range(i+1,len(sentence)):
        if sentence[i] == sentence[j]:
            result.append(sentence[i])
            flag = True
            break
    if flag:
        break
if len(result) == 0:
    print(f'No Repeated Word Here...!!!')
else:
    print(f'First Repeated Word is {result[0]}')