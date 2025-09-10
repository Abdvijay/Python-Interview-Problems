# Enter the list elements : 1 2 3 4 5
# Enter the k value : 2
# Before Left Rotating : [1, 2, 3, 4, 5]
# After Left Rotating : [3, 4, 5, 1, 2]

lst = list(map(int,input("Enter the list elements : ").split()))
k = int(input("Enter the k value : "))
print(f'Before Left Rotating : {lst}')
k = k % len(lst)
result = [lst[(i+k) % len(lst)] for i in range(len(lst))]
print(f'After Left Rotating : {result}')