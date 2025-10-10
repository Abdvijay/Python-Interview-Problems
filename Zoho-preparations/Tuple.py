from functools import reduce

tup = (1,2,3,4,5)

print("1. Printing tuple values                     : ",tup)

lst = list(tup)
lst.extend([6,6,6])
tup = tuple(lst)
print("2. After adding values using list            : ",tup)

tup = tuple(set(tup))
print("3. After removing duplicates using set       : ",tup)

print("4. Fetching values using indexing            : ",tup[0])

print("5. Fetching values using slicing             : ",tup[0:4])

print("6. Fetching values using negative indexing   : ",tup[-1])

print("7. Printing values in reverse using indexing : ",tup[::-1])

print("8. After sorting a tuple using sorted        : ",tuple(sorted(tup)))

print("9. Count values using count method           : ",tup.count(6))

print("10. Finding value's index                    : ",tup.index(4))

print("11. Finding len of the tuple                 : ",len(tup))

print("12. Printing squares of each values          : ",tuple(map(lambda x: x*x,tup)))

print("13. Printing even number only using filter   : ",tuple(filter(lambda x: x % 2 ==0,tup)))

print("14. Finding products using reduce            : ",reduce(lambda a,b: a * b,tup))

a, *b = tup
print("15. After using unpacking tuple              : ",a,",",b)

print("16. After using list comprehension concept   : ",tuple(x * 2 for x in tup))

print("17. After using repitation concept           : ",tup * 2)

print("18. Check values inside tup or not           : ",["True" if 2 in tup else "False"])