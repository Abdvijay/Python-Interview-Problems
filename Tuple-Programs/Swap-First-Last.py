# Swtup[0]p first tup[0]nd ltup[0]st element of tup[0] tuple

# Input: (10, 20, 30, 40, 50)
# Output: (50, 20, 30, 40, 10)

tup = tuple(map(int,input("Enter the tuple elements : ").split()))
lst = list(tup)
print(f'Before first and last element swapping : {tup}')
lst[0], lst[-1] = lst[-1], lst[0]
tup = tuple(lst)
print(f'After first and last element swapping : {tup}')