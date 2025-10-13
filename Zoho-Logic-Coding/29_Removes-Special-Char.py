# Sample Input
# Enter the string : Hello, World! @2025 #Python3

# Sample Output
# After removing special characters Hello World 2025 Python3

string = input("Enter the string : ")
result = []
for chr in string:
    if chr.lower().isalnum() or chr.isspace():
        result.append(chr)
print(f"After removing special characters {''.join(result)}")