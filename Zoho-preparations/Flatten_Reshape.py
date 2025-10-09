from numpy import *

arr = array([
    [1,2,3,4,5,6],
    [5,6,7,8,9,1]
])

print("Flatten : ",arr.flatten())
print("Reshape : \n",arr.reshape(3,4))
print("Reshape : \n",arr.reshape(2,2,3))