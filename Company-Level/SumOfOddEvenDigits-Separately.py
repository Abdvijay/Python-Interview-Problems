# Find Sum of Odd and Even Digits Separately

# Input: 12345

# Output: Odd Sum = 9, Even Sum = 6

number = input("Enter the number : ")
odd_sum = sum([int(i) for i in number if int(i) % 2 != 0])
even_sum = sum([int(i) for i in number if int(i) % 2 == 0])
print(f'Sum of Odd Digits : {odd_sum}')
print(f'Sum of Even Digits : {even_sum}')