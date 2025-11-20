lst = []
for i in range(3):
    num = int(input(f"Enter the number {i+1} : "))
    lst.append(num)
lst.sort()
print(f'Largest amoung {lst} is {lst[-1]}')

# OUTPUT

# Enter the number : 3
# Enter the number : 4
# Enter the number : 1
# Largest amoung [1, 3, 4] is 4