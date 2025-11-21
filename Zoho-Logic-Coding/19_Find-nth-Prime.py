# Sample Input
# Enter the nth value : 5

# Sample Output
# The 5th prime number is : 11

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2,num):
#         if num % i == 0:
#             return False
#     return True

# def nth_prime(number):
#     count = 0
#     num = 1
#     while count < number:
#         num += 1
#         if is_prime(num):
#             count += 1
#     return num

# number = int(input("Enter the nth value : "))
# print(f"The {number}th prime number is : {nth_prime(number)}")

import itertools
nth_prime = int(input("Enter the number to find nth prime : "))
prime = []
for i in itertools.count():
    flag = True
    if i == 0 or i == 1:
        continue
    else:
        for j in itertools.count():
            if j == 0 or j == 1:
                continue
            else:
                if i < j:
                    break
                else:
                    if i % j == 0 and i != j:
                        flag = False
                        break
    if flag:
        prime.append(i)

    if len(prime) == nth_prime:
        break
print(f'{nth_prime} prime number is {prime[-1]} and prime numbers are {prime}')

# Enter the number to find nth prime : 6
# 6 prime number is 13 and prime numbers are [2, 3, 5, 7, 11, 13]