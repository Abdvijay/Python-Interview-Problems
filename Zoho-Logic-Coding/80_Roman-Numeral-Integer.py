roman = input("Enter Roman numeral: ")

values = {
    'I': 1, 'V': 5, 'X': 10,
    'L': 50, 'C': 100, 'D': 500, 'M': 1000
}

total = 0
prev = 0

for char in reversed(roman):
    current = values[char]

    if current < prev:
        total -= current
    else:
        total += current

    prev = current

print(total)

# Sample Input and Sample Output

# Enter Roman numeral: IV
# 4

# Enter Roman numeral: VIII
# 8

# Enter Roman numeral: LVIII
# 58

# Enter Roman numeral: MCMXCIV
# 1994