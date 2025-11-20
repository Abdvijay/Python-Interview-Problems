word = input("Enter the string : ")
result = {}
for i in word:
    if i not in result:
        result[i] = 1
    else:
        result[i] += 1
for i in word:
    if result[i] == 1:
        print(f"First Non Repeated Character is {i}")
        break

# OUTPUT

# Enter the string : THALAPATHY
# First Non Repeated Character is L