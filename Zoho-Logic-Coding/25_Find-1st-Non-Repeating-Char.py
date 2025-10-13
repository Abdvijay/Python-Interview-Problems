# Sample Input
# Enter the string : geeksforgeeks

# Sample Output
# First non repeating char in a string geeksforgeeks is f

string = input("Enter the string : ")
non_repeating_char = {}
for chr in string:
    if chr not in non_repeating_char:
        non_repeating_char[chr] = 1
    else:
        non_repeating_char[chr] += 1
for key,values in non_repeating_char.items():
    if values == 1:
        print(f"First non repeating char in a string {string} is {key}")
        break