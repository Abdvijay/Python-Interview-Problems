# Sample Input
# Enter the list elements : 1 5 4 3 2
# Before sorting : [1, 5, 4, 3, 2]

# Sample Output
# After sorting : [1, 2, 3, 4, 5]

def bubble(lst):
    for i in range(len(lst)):
        for j in range(0,len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

lst = list(map(int,input("Enter the list elements : ").split()))
print(f"Before sorting : {lst}")
print(f"After sorting : {bubble(lst)}")