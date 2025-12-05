# Input:
# "Python is fun and Python is powerful"

# Output:

# Python: 2
# is: 2
# fun: 1
# and: 1
# powerful: 1

sentence = list(map(str,input("Enter the sentence : ").split()))
result = {}
for word in sentence:
    if word not in result:
        result[word] = 1
    else:
        result[word] += 1
for key,value in result.items():
    print(f'{key} : {value}')