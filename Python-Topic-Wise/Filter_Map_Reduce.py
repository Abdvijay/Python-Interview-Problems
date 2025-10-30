# I. map() - Applies an function to each element in an iterator and produce an map object. 
#          - To view the result map object must be convert into list or tuple or set.
#          - Simply says transform each element or apply same operation to all element.

# 1. Finding square of a list using simple normal map() function

nums = [1,2,3,4,5]
squares = list(map(lambda n : n * n,nums))
print(f'1. Finding square of a each element using map()                                 : {squares}')

# 2. Converting type of each element using map() function

nums = [1,2,3,4,5]
print(f'2. Converting each element from int to str using map()                          : {list(map(str,nums))}')

# 3. Converting temparature from celcius to fareheit without lambda in map()

def temp(c):
    return (c * 9/5) + 32

celcius = [10,20,30]
fareheit = list(map(temp,celcius))
print(f'3. Finding temparature without lambda function inside map()                     : {fareheit}')

# 4. Adding two list element wise using map()

a = [1,2,3]
b = [4,5,6]
sum_list = list(map(lambda x,y : x+y,a,b))
print(f"4. Adding two list element wise using map()                                     : {sum_list}")

# 5. use in built function inside map() and return as dictionary

words = ["Vijay","Deeksha","Swathi"]
length = list(map(len,words))
print(f'5. use built in function inside map() return as dictionary                      : {dict(zip(words,length))}')

# II. Filter - Select elements based on condition and retuns an iterator like map().
#            - When you want to filter out elements that meet a certain condition (like even numbers, positive numbers, etc.).

# 6. Filter even numbers from a list using filter()

nums = [1,2,3,4,5,6,7,8,9]
evens = list(filter(lambda x: x % 2 == 0,nums))
print(f'6. Filter even numbers only from a list using filter()                          : {evens}')

# 7. Filter words which is longer than 3(len) using filter()

words = ["Vijay","is","a","Good"]
length = filter(lambda word: len(word) > 3,words)
print(f'7. Filter words which is longer than 3(len) using filter()                      : {list(length)}')

# 8. Find Palindrome words without using lambda in filter()

def palindrome(word):
    return word == word[::-1]

words = ['level','madam','vijay']
result = list(filter(palindrome,words))
print(f"8. Find Palindrome words without using lambda in filter()                       : {result}")

# 9. Filter name starting with 'A' using filter()

names = ['Atchaya','Aarthi','Vijay']
a_start_names = list(filter(lambda word: word.startswith('A'),names))
print(f'9. Filter name which is starting with "A" using filter()                        : {a_start_names}')

# 10. Finding all positive numbers only using filter() without lambda convert into tuple

def pos(num):
    return num > 0

nums = [0,4,-2,-5,3,-7]
positives = tuple(filter(pos,nums))
print(f'10. Finding all positive numbers in tuple using filter() without lambda         : {positives}')

# 11. Sum of all numbers using reduce()

from functools import reduce

nums = [1,2,3,4,5]
total = reduce(lambda x,y: x+y,nums)
print(f'11. Sum of all numbers {nums} using reduce()                           : {total}')

# 12. Product of all numbers using filter() without lambda

from functools import reduce

def multiply(a,b):
    return a * b

nums = [1,2,3,4,5]
product = reduce(multiply,nums)
print(f'12. Product of all numbers {nums} without lambda using reduce()        : {product}')

# 13. Find maximum of value using filter()

from functools import reduce

nums = [1,53,34,67,35,23]
maximum = reduce(lambda x,y: x if x > y else y,nums)
print(f'13. Maximum of value {nums} using reduce()                     : {maximum}')

# 14. Concatenate strings using reduce()

from functools import reduce

words = ["Python","is","awesome"]
print(f'14. Concatenate string using reduce()                                           : {reduce(lambda x,y: x + " " + y,words)}')

# 15. Sum with initializer using in reduce()

from functools import reduce

nums = [10,20,30,40,50]
print(f'15. Sum of all elements {nums} with initializer using in reduce() : {reduce(lambda a,b: a + b,nums,100)}')

# Output : (map,filter,reduce)

# 1. Finding square of a each element using map()                                 : [1, 4, 9, 16, 25]
# 2. Converting each element from int to str using map()                          : ['1', '2', '3', '4', '5']
# 3. Finding temparature without lambda function inside map()                     : [50.0, 68.0, 86.0]
# 4. Adding two list element wise using map()                                     : [5, 7, 9]
# 5. use built in function inside map() return as dictionary                      : {'Vijay': 5, 'Deeksha': 7, 'Swathi': 6}
# 6. Filter even numbers only from a list using filter()                          : [2, 4, 6, 8]
# 7. Filter words which is longer than 3(len) using filter()                      : ['Vijay', 'Good']
# 8. Find Palindrome words without using lambda in filter()                       : ['level', 'madam']
# 9. Filter name which is starting with "A" using filter()                        : ['Atchaya', 'Aarthi']
# 10. Finding all positive numbers in tuple using filter() without lambda         : (4, 3)
# 11. Sum of all numbers [1, 2, 3, 4, 5] using reduce()                           : 15
# 12. Product of all numbers [1, 2, 3, 4, 5] without lambda using reduce()        : 120
# 13. Maximum of value [1, 53, 34, 67, 35, 23] using reduce()                     : 67
# 14. Concatenate string using reduce()                                           : Python is awesome
# 15. Sum of all elements [10, 20, 30, 40, 50] with initializer using in reduce() : 250