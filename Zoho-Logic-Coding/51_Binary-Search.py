# Linear Search

# Sample Input
# Enter the list elements : 1 4 3 2 5
# Enter the element to search : 3

# Sample Output
# The element 3 found in [1, 4, 3, 2, 5] at position is 2

# lst = list(map(int,input("Enter the list elements : ").split()))
# value = int(input("Enter the element to search : "))
# count = 0
# for i in lst:
#     if i == value:
#         print(f"The element {value} found in {lst} at position is {count}")
#         break
#     else:
#         count += 1

# Binary Search

# Sample Input
# Enter the list elements : 1 2 4 7 6 5
# Enter the target value : 5

# Sample Output
# The element found at position 3

def binary_search(sorted_lst,target_value):
    start = 0
    end = (len(sorted_lst)) - 1
    while start <= end:
        mid = ( start + end ) // 2
        if sorted_lst[mid] == target_value:
            return mid
        elif sorted_lst[mid] < target_value:
            start = mid + 1
        else:
            end = mid - 1
    return -1

lst = list(map(int,input("Enter the list elements : ").split()))
lst.sort()
target = int(input("Enter the target value : "))
result = binary_search(lst,target)
print(f"The element found at position {result}")