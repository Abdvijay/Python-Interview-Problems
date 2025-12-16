sentence = input("Enter the sentence to check Palindrome : ")
non_alpha = []
for ch in sentence:
    if ch.isalpha():
        non_alpha.append(ch.lower())
non_alpha = "".join(non_alpha)
rev = "".join(list(reversed(non_alpha)))
if non_alpha == rev:
    print(f'Given sentence "{sentence}" is Valid Palindrome')
else:
    print(f'Given sentence "{sentence}" is not a Valid Palindrome')

# Sample Input and Sample Output

# Enter the sentence to check Palindrome : Madam, I'm Adam
# Given sentence "Madam, I'm Adam" is Valid Palindrome

# Enter the sentence to check Palindrome : Was it a car or a cat I saw?
# Given sentence "Was it a car or a cat I saw?" is Valid Palindrome

# Enter the sentence to check Palindrome : No 'x' in Nixon
# Given sentence "No 'x' in Nixon" is Valid Palindrome

# Enter the sentence to check Palindrome : Hello, World!
# Given sentence "Hello, World!" is not a Valid Palindrome