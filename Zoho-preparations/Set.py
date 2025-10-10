from functools import reduce

sets = {1,3,5,2,4,5,3,2,4}

print("1. Printing set values                       : ",sets)

sets.add(10)
print("2. After add one value                       : ",sets)

sets.update([11,21])
print("3. After update a value                      : ",sets)

print("4. After sorted set                          : ",set(sorted(sets)))

sets.remove(21)
print("5. After removing value                      : ",sets)

sets.pop()
print("6. After using pop in sets                   : ",sets)

sets.discard(22)
print("7. After using discard in sets               : ",sets)

a = {1,2,3}
b = {2,4,5}

print("8. Union operation                           : ",a.union(b))

print("9. Intersectin operation                     : ",a.intersection(b))

print("10. Difference (a-b) operation               : ",a.difference(b))

print("11. Difference (b-a) operation               : ",b.difference(a))

print("12. Symmetric Difference operation           : ",a.symmetric_difference(b))

a.update(b)
print("13. Update operation                         : ",a)

a.intersection_update(b)
print("14. Intersection_update operation            : ",a)

a.difference_update(b)
print("15. Difference_update operation              : ",a)

a.symmetric_difference_update(b)
print("16. Symmetric_difference_update operation    : ",a)

print("17. After using map function using in lambda : ",set(map(lambda x:x*x,sets)))

print("18. After using filter using in lambda       : ",set(filter(lambda x:x%2 == 0,sets)))

print("19. After using reduce using in lambda       : ",reduce(lambda x,y: x * y,sets))

a = {1,2,3}
b = {2}
print("20. issubset function                        : ",a.issubset(b))

print("21. issuper function                         : ",a.issuperset(b))

a = {1,2,3}
b = {5,4,7}
print("22. isdisjoint function                      : ",a.isdisjoint(b))

print("23. Finding len of sets using len()          : ",len(sets))