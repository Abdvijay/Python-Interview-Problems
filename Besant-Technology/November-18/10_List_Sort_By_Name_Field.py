list1=[["student101","Vijay",25],["student105","Deeksha",6],["student103","Swathi",28]]
print(list1)
n=len(list1)
for i in range(n-1,-1,-1):
    for j in range(0,i):
        if(list1[j][1]>list1[j+1][1]):
            temp=list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=temp
print(list1)

# OUTPUT

# [['student101', 'Vijay', 25], ['student105', 'Deeksha', 6], ['student103', 'Swathi', 28]]
# [['student105', 'Deeksha', 6], ['student103', 'Swathi', 28], ['student101', 'Vijay', 25]]