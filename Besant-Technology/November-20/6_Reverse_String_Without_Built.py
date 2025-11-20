word = input("Enter the string to reverse : ")
temp = word
result = []
for i in range(len(temp),0,-1):
    result.append(temp[i-1])
print(f'Original String is {word} and Reverse String is {"".join(result)}')

# OUTPUT

# Enter the string to reverse : python
# Original String is python and Reverse String is nohtyp