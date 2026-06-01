# Sample Input
# Enter the string : madam

# Sample Output
# The frequency of each char in a string madam is {'m': 2, 'a': 2, 'd': 1}

string = input("Enter the string : ")
freq = {}
for chr in string:
    if chr not in freq:
        freq[chr] = 1
    else:
        freq[chr] += 1
print(f"The frequency of each char in a string {string} is {freq}")

# Simplest way to count frequency of each char in a string using count method
# string = input("Enter the string : ")
# freq = {}
# for letter in string:
#     if letter not in freq:
#         freq[letter] = string.count(letter)
# print(f"Frequency of each character in a string {string} is {freq}")