# Check Automorphic Number

# (Number whose square ends with the same number)

# Input: 25 → 25² = 625

# Output: Automorphic

# Input: 7 → 7² = 49

# Output: Not Automorphic

number = int(input("Enter the number to be check : "))
temp = number
sq = number * number
digit = sq % (10 ** len(str(number)))
if number == digit:
    print(f'The given number {temp} is Automorphic')
else:
    print(f'The given number {temp} is not an Automorphic')