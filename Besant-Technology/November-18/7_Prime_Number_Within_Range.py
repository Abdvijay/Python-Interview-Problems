start = int(input("Enter the start range : "))
end = int(input("Enter the end range : "))
result = []
for i in range(start,end+1):
    is_prime = True
    for j in range(2,i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        result.append(i)
print(f"Prime numbers between {start} and {end} is {result}")

# OUTPUT

# Enter the start range : 25
# Enter the end range : 50
# Prime numbers between 25 and 50 is [29, 31, 37, 41, 43, 47]