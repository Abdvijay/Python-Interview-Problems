# Sample Input
# Enter the sentence : hi vijay how are you

# Sample Output
# After changing title case in sentence : Hi Vijay How Are You

sentence = input("Enter the sentence : ").split()
result = []
for word in sentence:
    title_case = word[0].upper() + word[1:].lower()
    result.append(title_case)
print(f"After changing title case in sentence : {' '.join(result)}")