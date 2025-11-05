# List Comprehension

# Definition : 

#   1. It provides a way to create al lists using single line of code instead of loops.
#   2. It returns a new list.
#   3. You can use conditions inside comprehension.
#   4. Nested loops can also be used.

# Syntax :

#   [expression for item in iterable condition]

# 1. Simple program - Find square of a number using List Comprehension

nums = [1,2,3,4,5]
squares = [n * n for n in nums]
print(f"1. Find Square of a number using List comprehension (Simple)          : {squares}")

# 2. With Condition - Find even numbers only
nums = [1,2,3,4,5,6]
evens = [n for n in nums if n % 2 == 0]
print(f"2. Find even numbers only using List Comprehension (With Condition)   : {evens}")

# 3. With Expression +  Condition - Find Square of even numbers only
nums = [1,2,3,4,5,6]
evens_squares = [n * n for n in nums if n % 2 == 0]
print(f"3. Find Squares of even numbers only (With Expression + Condition)    : {evens_squares}")

# 4. String operations
names = ['vijay','swathi','deeksha']
up_names = [name.upper() for name in names]
print(f"4. Change to uppercase using List Comprehension (In String Operation) : {up_names}")

# 5. With if else condition
nums = [1,2,3,4,5]
result = ["Even" if n % 2 == 0 else "Odd" for n in nums]
print(f"5. Find Odd or Even using List Comprehension (With If Else Condition) : {result}")

# 6. Nested List Comprehension
matrix = [[1,2,3],[4,5,6],[7,8]]
result = [n for row in matrix for n in row]
print(f"6. Flattened a list (With Nested List Comprehension Condition)        : {result}")

# 7. Comprehension with Range
nums = [i for i in range(1,6)]
print(f"7. Creating a list (Comprehension With Range)                         : {nums}")

# 8. Extracting using List Comprehension with String operations
names = ['vijay','swathi','deeksha','laksh']
first_letter = [name[0] for name in names]
print(f"8. First letter using List Comprehension (Extracting)                 : {first_letter}")

# 9. Nested Condition
nums = [10,20,30,40,50]
result = ["High" if num > 20 else "Low" if num < 15 else "Medium" for num in nums]
print(f"9. Finding low,medium,high (With Nested Condition)                    : {result}")

# 10. Convert list of values string into integers
str_nums = ["10","20","30"]
int_nums = [int(x) for x in str_nums]
print(f"10. Convert list of values string into integers (With Converting)     : {int_nums}")

# Output 

# 1. Find Square of a number using List comprehension (Simple)          : [1, 4, 9, 16, 25]
# 2. Find even numbers only using List Comprehension (With Condition)   : [2, 4, 6]
# 3. Find Squares of even numbers only (With Expression + Condition)    : [4, 16, 36]
# 4. Change to uppercase using List Comprehension (In String Operation) : ['VIJAY', 'SWATHI', 'DEEKSHA']
# 5. Find Odd or Even using List Comprehension (With If Else Condition) : ['Odd', 'Even', 'Odd', 'Even', 'Odd']
# 6. Flattened a list (With Nested List Comprehension Condition)        : [1, 2, 3, 4, 5, 6, 7, 8]
# 7. Creating a list (Comprehension With Range)                         : [1, 2, 3, 4, 5]
# 8. First letter using List Comprehension (Extracting)                 : ['v', 's', 'd', 'l']
# 9. Finding low,medium,high (With Nested Condition)                    : ['Low', 'Medium', 'High', 'High', 'High']
# 10. Convert list of values string into integers (With Converting)     : [10, 20, 30]