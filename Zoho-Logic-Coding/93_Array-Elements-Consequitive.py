lst = list(map(int,input("Enter the list elements : ").split()))
diff = []
for i in range(len(lst)):
    if i+1 == len(lst):
        break
    value = lst[i] - lst[i+1]
    diff.append(value)

if all(i == diff[0] for i in diff):
    print("True")
else:
    print("False")

# Sample Input and Sample Output

# Enter the list elements : 1 2 3 4
# True

# Enter the list elements : 4 3 2 1
# True

# Enter the list elements : 1 3 4 6
# False

# Enter the list elements : 1 3 5 7
# True

# Enter the list elements : 10
# True