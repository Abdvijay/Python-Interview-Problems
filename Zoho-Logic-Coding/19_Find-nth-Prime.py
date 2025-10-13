# Sample Input
# Enter the nth value : 5

# Sample Output
# The 5th prime number is : 11

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def nth_prime(number):
    count = 0
    num = 1
    while count < number:
        num += 1
        if is_prime(num):
            count += 1
    return num

number = int(input("Enter the nth value : "))
print(f"The {number}th prime number is : {nth_prime(number)}")