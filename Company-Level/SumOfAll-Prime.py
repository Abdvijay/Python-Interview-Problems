number = int(input("Enter the number : "))
result = []
for i in range(2,number):
    if i <= 3:
        result.append(i)
    else:
        flag = False
        for j in range(2,i+1):
            if i % j == 0 and i != j:
                flag = False
                break
            else:
                flag = True
        if flag:
            result.append(i)
print(f'The prime number upto {number} is {result} and its sum is {sum(result)}')