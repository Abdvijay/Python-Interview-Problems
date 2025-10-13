# Sample Input
# Enter the string : geeksforgeeks

# Sample Output
# After removing duplicates from string is `geksfor`

string = input("Enter the string : ")
final = []
for chr in string:
    if chr not in final:
        final.append(chr)
print(f"After removing duplicates from string is `{''.join(final)}`")