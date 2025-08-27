number = int(input("Enter the number to be check : "))
temp = number
sq = number * number
digit = sq % (10 ** len(str(number)))
if number == digit:
    print(f'The given number {temp} is Automorphic')
else:
    print(f'The given number {temp} is not an Automorphic')