lst = list(map(int,input("Enter the list elements : ").split()))
k = int(input("Enter the k value : "))
print(f'Before Left Rotating : {lst}')
k = k % len(lst)
result = [lst[(i+k) % len(lst)] for i in range(len(lst))]
print(f'After Left Rotating : {result}')