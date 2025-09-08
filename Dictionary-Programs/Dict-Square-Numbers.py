# Create dictionary of squares of numbers

# Input: n=5
# Output: {1:1, 2:4, 3:9, 4:16, 5:25}

n = int(input("Enter the number : "))
dic = {}
for i in range(1,n+1):
    dic[i] = i * i
print(dic)