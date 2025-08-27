# Print Numbers in Words

# Input: 507

# Output: "Five Hundred and Seven"


number = int(input("Enter the 3 digit number : "))
ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]
words = ""
temp = number

if number == 0:
    words += "Zero"

#Handle Hundreds
if number >= 100:
    words += ones[number // 100] + " Hundred"
    number = number % 100
    if number != 0:
        words += " and "

#Handle Remaining
if number < 20:
    words += ones[number]
else:
    words += tens[number // 10]
    if number % 10 != 0:
        words += " " + ones[number % 10]
print(f'The given number {temp} -> {words}')