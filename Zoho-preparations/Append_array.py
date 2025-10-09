from array import *

arr = array('i',[])
size = int(input("Enter the array size : "))
print("Enter the array values : ")
for i in range(size):
    x = int(input())
    arr.append(x)
print("Final array : ",arr)