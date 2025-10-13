# Sample Input
# Enter the string to check palindrome or not : madam

# Sample Output
# The given string madam is palindrome

string = input("Enter the string to check palindrome or not : ")
if string == string[::-1]:
    print(f"The given string {string} is palindrome")
else:
    print(f"The given string {string} is not an palindrome")