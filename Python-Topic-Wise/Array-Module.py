# Array Definition :

#       In Python, array is a collection of items stored at contiguous memory locations. 
#       The idea is to store multiple items of the same type together.

# Creation:

#        array.array(typecode, [initializer]): Creates an array with a specified typecode (e.g., 'i' for signed int, 'f' for float) and 
#        an optional initializer list.

# Methods:

#        Many methods are similar to lists: append(), extend(), insert(), pop(), remove(), index(), count(), reverse().

from array import *

# 1. Creation of an array

arr = array('i',[1,2,3])
print(arr) # array('i', [1, 2, 3])

# 2. Adding element using append() :

arr = array('i',[])
for i in range(5):
    arr.append(i)
print(arr) # array('i', [0, 1, 2, 3, 4])

# 3. Adding element using extend()

arr = array('i',[])
arr.extend([1,2,3,4,5])
print(arr) # array('i', [1, 2, 3, 4, 5])

# 4. Adding element using insert()

arr = array('i',[1,2,3,4,5])
arr.insert(2,100)
print(arr) # array('i', [1, 2, 100, 3, 4, 5])

# 5. Removing element using pop()

arr = array('i',[1,2,3,4,5])
print(arr) # array('i', [1, 2, 3, 4, 5])
arr.pop()
print(arr) # array('i', [1, 2, 3, 4])

# 6. Removing element using remove()

arr = array('i',[1,2,3,4,5])
print(arr) # array('i', [1, 2, 3, 4, 5])
arr.remove(4)
print(arr) # array('i', [1, 2, 3, 5])

# 7. Find index of value

arr = array('i',[1,2,3,4,5])
print(f'Index of 3 is {arr.index(3)}') # Index of 3 is 2

# 8. Counting the values

arr = array('i',[1,2,1,3,5,6,2,1])
print(f'Total count of 1 is {arr.count(1)}') # Total count of 1 is 3

# 9. Finding length of the array using len()

arr = array('i',[1,4,5,3,2])
print(f'Length of an array is {len(arr)}') # Length of an array is 5

# 10. Printing array in reverse order using reverse()

arr = array('i',[1,5,4,3,2])
arr.reverse()
print(f'Reverse of an array {arr}') # Reverse of an array array('i', [2, 3, 4, 5, 1])