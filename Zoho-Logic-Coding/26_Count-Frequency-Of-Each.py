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