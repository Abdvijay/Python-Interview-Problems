# Enter the list elements : 1 2 3 4 5
# Enter the k value : 2
# Before Right Rotating : [1, 2, 3, 4, 5]
# After Right Rotating : [4, 5, 1, 2, 3]

lst = list(map(int,input("Enter the list elements : ").split()))
k = int(input("Enter the k value : "))
k = k % len(lst)
print(f'Before Right Rotating : {lst}')
result = [lst[(i-k) % len(lst)] for i in range(len(lst))]
print(f'After Right Rotating : {result}')