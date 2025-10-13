# Sample Input
# Enter the sequences of list values : 1 2 4 7 9

# Sample Output
# Missing sequences : [3, 5, 6, 8]

sequence = list(map(int,input("Enter the sequences of list values : ").split()))
result = []
start,end = sequence[0],sequence[-1]
for i in range(start,end):
    if i not in sequence:
        result.append(i)
print(f"Missing sequences : {result}")