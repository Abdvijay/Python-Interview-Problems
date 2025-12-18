lst = list(map(int,input("Enter the list elements : ").split()))
low = int(input("Enter the low value : "))
high = int(input("Enter the high value : "))
result = []
temp = []
dummy = []
for i in range(low,high+1):
    if i not in lst:
        temp.append(i)
    else:
        if temp:
            if len(temp) > 1:
                dummy.append(str(temp[0]))
                dummy.append(str(temp[-1]))
                result.append("-".join(dummy))
            else:
                result.append(str(temp[0]))
            dummy = []
            temp = []
        else:
            pass
if temp:
    dummy.append(str(temp[0]))
    dummy.append(str(temp[-1]))
    result.append("-".join(dummy))
print(result)

# Sample Input and Sample Output

# Enter the list elements : 4 9 14
# Enter the low value : 0
# Enter the high value : 100
# ['0-3', '5-8', '10-13', '15-100']

# Enter the list elements : 0 1 3 50 75
# Enter the low value : 0
# Enter the high value : 99
# ['2', '4-49', '51-74', '76-99']