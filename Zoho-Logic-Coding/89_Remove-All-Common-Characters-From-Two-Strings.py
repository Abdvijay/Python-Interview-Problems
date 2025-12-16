str1 = input("Enter the string - 1 : ")
str2 = input("Enter the string - 2 : ")

result = []
unique = []
repeated = []
for i in str1:
    flag = True
    for j in str2:
        if i == j:
            if i not in repeated:
                repeated.append(i)
            flag = False
            break
        else:
            pass
    if flag:
        unique.append(i)

if len(unique):
    result.append("".join(unique))
unique = []

for j in str2:
    if j not in repeated:
        unique.append(j)

if len(unique):
    result.append("".join(unique))

if len(result) == 0:
    print(f"Empty Strings")
else:
    print(f"After removing all common characters {" ".join(result)}")

# Sample Input and Sample Output

# Enter the string - 1 : python
# Enter the string - 2 : java
# After removing all common characters python java

# Enter the string - 1 : test 
# Enter the string - 2 : text
# After removing all common characters s x

# Enter the string - 1 : abc
# Enter the string - 2 : abc
# Empty Strings

# Enter the string - 1 : hello
# Enter the string - 2 : world
# After removing all common characters he wrd