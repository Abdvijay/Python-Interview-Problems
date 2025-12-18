lst = list(map(int,input("Enter the list elements : ").split()))
possible_sub_array = []
temp = []
for i in range(len(lst)):
    possible_sub_array.append([lst[i]])
    temp.append(lst[i])
    for j in range(i+1,len(lst)):
        temp.append(lst[j])
        possible_sub_array.append(temp.copy())
    temp = []

maximum = 0
for sub_array in possible_sub_array:
    total = 1
    for i in sub_array:
        total *= i

    if total > maximum:
        maximum = total
        result_sub_array = []
        result_sub_array.append(sub_array)
print(f'Maximum product of sub array is {maximum} and the sub array is {result_sub_array[0]}')

# Sample Input and Sample Output

# Enter the list elements : 2 4 1 -5 3 8 1
# Maximum product of sub array is 24 and the sub array is [3, 8]

# Enter the list elements : 2 3 -2 4      
# Maximum product of sub array is 6 and the sub array is [2, 3]