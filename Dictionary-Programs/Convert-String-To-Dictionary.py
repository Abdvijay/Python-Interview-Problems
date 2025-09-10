# Convert two strings into dictionary (keys, values)

# Input: "name age city", "Alice 25 Paris"
# Output: {'name':'Alice', 'age':'25', 'city':'Paris'}

string1 = input("Enter the string 1 : ").split()
string2 = input("Enter the string 2 : ").split()
str1 = []
str2 = []
for key in string1:
    str1.append(key)
for key in string2:
    str2.append(key)
result = dict(zip(str1,str2))
print(result)