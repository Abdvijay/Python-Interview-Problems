from functools import reduce
lst = [1,2,3,4,5]

print("1. Printing List values                : ",lst)

lst.append(6)
print("2. After using append                  : ",lst)

lst.extend([7,8,9])
print("3. After using extent                  : ",lst)

lst.insert(2,9)
print("4. After using insert                  : ",lst)

print("5. After using count                   : ",lst.count(9))

ind = lst.index(9)
# ind1 = lst.index(10)
print("6. After using index                   : ",ind)
# print("After using index  : ",ind1)

lst.pop()
print("7. After using pop                     : ",lst)

lst.remove(9)
print("8. After using remove                  : ",lst)

lst.reverse()
print("9. After using reverse                 : ",lst)

lst.sort()
print("10. After using sort                   : ",lst)
lst.sort(reverse=True)
print("11. After using sort(rev)              : ",lst)

sort_list = lst[::-1]
print("12. Sorting using indexing             : ",sort_list)

print("13. Fetch using indexing               : ",sort_list[2])

print("14. Slicing values [2:6]               : ",sort_list[2:6])

print("15. Find squares using lambda in list  : ",list(map(lambda x: x*x,sort_list)))

print("16. Find evens using lambda in list    : ",list(filter(lambda x: x % 2 == 0,sort_list)))
 
print("17. Find products of list using reduce : ",reduce(lambda x,y: x*y,sort_list))

del sort_list[-1]
print("18. After deleting last item using del : ",sort_list)

print("19. Iterating list using for loop      : ",end=" ")
for i in sort_list:
    print(i,end=" ")

print("")
print("20. Collaberating list comprehension   : ",[x*2 for x in sort_list])

copied_lst = sort_list.copy()
print("21. Copied list using copy method      : ",copied_lst)

copied_lst.clear()
print("22. After using clear method in list   : ",copied_lst)

print("23. Calculating a len of sorted_lst    : ",len(sort_list))

print("24. After using split method to list   : ","vijay deeksha swathi laksh".split())

print("25. Calculating total using sum        : ",sum(sort_list))

print("26. Finding minimum of value from list : ",min(sort_list))

print("27. Finding maximum of value from list : ",max(sort_list))

print("28. Decreasing values from list        : ",[x-1 for x in sort_list])

print("29. After using repitation concept     : ",sort_list * 2)

print("30. Checking values inside list or not : ",[True if 5 in sort_list else False])