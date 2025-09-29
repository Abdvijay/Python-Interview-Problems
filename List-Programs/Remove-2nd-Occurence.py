# Question : Write a Python program to remove a number from a list at its specified occurrence position ?

numbers = [10,20,30,40,50,10,10,20,30,10]
removable_number = int(input("Enter the removable number : "))
occurence_number = int(input("Enter the occurence number : "))
result = {}
final = []
print("Before removing : ",numbers)
for num in numbers:
    if num not in result:
        result[num] = 1
    else:
        result[num] += 1
    if num == removable_number and occurence_number == result[num]:
        pass
    else:
        final.append(num)
print("After removing  : ",final)

# Sample Output 1: 

# Enter the removable number : 10
# Enter the occurence number : 4
# Before removing :  [10, 20, 30, 40, 50, 10, 10, 20, 30, 10]
# After removing  :  [10, 20, 30, 40, 50, 10, 10, 20, 30]

# Sample Output 2: 

# Enter the removable number : 20
# Enter the occurence number : 2
# Before removing :  [10, 20, 30, 40, 50, 10, 10, 20, 30, 10]
# After removing  :  [10, 20, 30, 40, 50, 10, 10, 30, 10]