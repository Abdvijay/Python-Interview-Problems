from numpy import *

original_deep_arr = array([1,2,3,4,5])

#Deep copy
print("-----------Deep copy array------------")
deep_copy_arr = original_deep_arr.copy()
print("Before updating the value (original  array)    : ",original_deep_arr)
print("Before updating the value (deep copy array)    : ",deep_copy_arr)

original_deep_arr[2] = 100
print("After updating the value (original  array)     : ",original_deep_arr)
print("After updating the value (deep copy array)     : ",deep_copy_arr)

original_shallow_arr = array([1,2,3,4,5])

#Shallow copy
print("---------Shallow copy array----------")
shallow_copy_arr = original_shallow_arr.view()
print("Before updating the value (original  array)    : ",original_shallow_arr)
print("Before updating the value (shallow copy array) : ",shallow_copy_arr)

original_shallow_arr[2] = 100
print("After updating the value (original  array)     : ",original_shallow_arr)
print("After updating the value (shallow copy array)  : ",shallow_copy_arr)