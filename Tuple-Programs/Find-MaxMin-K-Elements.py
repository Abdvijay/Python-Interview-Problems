# Find maximum and minimum k elements in tuple

# Input: (5, 10, 2, 8, 15, 3) , k=2
# Output: Max: (15, 10), Min: (2, 3)

tup = tuple(map(int,input("Enter the tuple elements : ").split()))
k = int(input("Enter the k value : "))
maximum = sorted(tup,reverse=True)[:k]
minimum = sorted(tup)[:k]
print(f'Output : Max : {tuple(maximum)}, Min : {tuple(minimum)}')