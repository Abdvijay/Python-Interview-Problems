# Question : Find the combo of target value with the given list of numbers ?

numbers = list(map(int,input("Enter the list of numbers : ").split()))
target_value = int(input("Enter the target value : "))
final = []
print(numbers)
for i in range(0,len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] + numbers[j] == target_value:
            final.extend([(numbers[i],numbers[j])])
print(final)

# Sample Output 1 : 
# Enter the list of numbers : 1 2 3 4 5 6 7 8 9 10
# Enter the target value : 9
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [(1, 8), (2, 7), (3, 6), (4, 5)]

# Sample Output 2 :
# Enter the list of numbers : 1 2 3 4 5 6 7 8 9 10
# Enter the target value : 3
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [(1, 2)]