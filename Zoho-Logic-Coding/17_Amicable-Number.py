# Sample Input
# Enter the two number by space : 220 284

# Sample Output
# The numbers 220 and 284 are Amicable numbers

# Concept
# {220: 284, 284: 220}
# Amicable numbers are two different natural numbers where the sum of the proper divisors of each is equal to the other number. 
# For example, the smallest amicable pair is (220, 284):

    # Proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, and 110, which sum to 284.
    # Proper divisors of 284 are 1, 2, 4, 71, and 142, which sum to 220.

num = list(map(int,input("Enter the two number by space : ").split()))
sums = {}
for i in num:
    total = 0
    for j in range(1,i):
        if i % j == 0:
            total += j
    sums[i] = total
# print(sums)
if sums[num[0]] == num[1] and sums[num[1]] == num[0]:
    print(f"The numbers {num[0]} and {num[1]} are Amicable numbers")
else:
    print(f"The numbers {num[0]} and {num[1]} are not Amicable numbers")