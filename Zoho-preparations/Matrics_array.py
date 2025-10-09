from numpy import *

arr = array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

mat1 = matrix('1 2 3;4 5 6;7 8 9')
matrices = matrix(arr)
print("Maximum : ",matrices.max())
print("Minimum : ",matrices.min())
print("Diagonal: ",diagonal(matrices))
print("Addition: \n",mat1+matrices)
print("Multiply: \n",mat1*matrices)