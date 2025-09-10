# Enter the number : 10
# [2, 3, 5, 7]

number = int(input("Enter the number : "))
lst = []
for i in range(2,number+1):
    if i <= 3 :
        lst.append(i)
    else:
        flag = False
        for j in range(2,i+1):
            if i % j == 0 and i != j:
                flag = False
                break
            else:
                flag = True

        if flag:
            lst.append(i)
print(lst)