number = int(input("Enter the number to find prime factors : "))
prime_factors = []
for i in range(1,number):
    if number % i == 0:
        prime_factors.append(i)
print(f"Prime Factors of {number} is {prime_factors}")