# Sample Input
# Enter the list elements : 1 2 3 4 5
# Enter the k position : 2

# Sample Output
# List [1, 2, 3, 4, 5] After rotating right rotation is [4, 5, 1, 2, 3]
# List [1, 2, 3, 4, 5] After rotating left rotation is [3, 4, 5, 1, 2]

lst = list(map(int,input("Enter the list elements : ").split()))
k = int(input("Enter the k position : "))
k = k % len(lst)
right_rotate = [lst[(i-k) % len(lst)] for i in range(len(lst))]
print(f"List {lst} After rotating right rotation is {right_rotate}")

left_rotate = [lst[(i+k) % len(lst)] for i in range(len(lst))]
print(f"List {lst} After rotating left rotation is {left_rotate}")