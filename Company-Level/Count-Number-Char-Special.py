# Count Alphabets, Digits, and Special Characters

# Input: "Hello123@!"

# Output: Alphabets=5, Digits=3, Specials=2

word = input("Enter the characters : ")
Alphabets = 0
Digits = 0
Specials = 0
for ch in word:
    if ch.isalpha():
        Alphabets += 1
    elif ch.isalnum():
        Digits += 1
    else:
        Specials += 1
print(f'Alphabets = {Alphabets}, Digits = {Digits}, Specials = {Specials}')