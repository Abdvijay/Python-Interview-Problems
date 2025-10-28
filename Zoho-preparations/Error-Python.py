# 1. Syntax Error -> Raised when a syntax error occurs like missing ':'

# if 5 > 6
#     print("5 is not greater than 6")

# File "C:\Users\My_Sowriyam\eclipse-workspace\PythonInterviewProblems\Zoho-preparations\Error-Python.py", line 3
#     if 5 > 6
#             ^
# SyntaxError: expected ':'

# -------------------------------------------------------------------------------------------------------------------------------------

# 2. Indentation Error -? Raised when indentation is not correct

# def addition(a,b):
# print(a+b)
# addition(5,5)

# File "C:\Users\My_Sowriyam\eclipse-workspace\PythonInterviewProblems\Zoho-preparations\Error-Python.py", line 14
#     print(a+b)
#     ^
# IndentationError: expected an indented block after function definition on line 13

# -------------------------------------------------------------------------------------------------------------------------------------

# 3. Name Error ->	Raised when a variable does not exist

# print(scores)
# scores = 100

# ile "c:\Users\My_Sowriyam\eclipse-workspace\PythonInterviewProblems\Zoho-preparations\Error-Python.py", line 24, in <module>
#     print(scores)
#           ^^^^^^
# NameError: name 'scores' is not defined

# -------------------------------------------------------------------------------------------------------------------------------------

# 4. Type Error -> Raised when two different types are combined

# print(100 + "Vijay")

# File "c:\Users\My_Sowriyam\eclipse-workspace\PythonInterviewProblems\Zoho-preparations\Error-Python.py", line 34, in <module>
#     print(100 + "Vijay")
#           ~~~~^~~~~~~~~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# -------------------------------------------------------------------------------------------------------------------------------------

# 5. Value Error -> Raised when there is a wrong value in a specified data type

# print(int("Vijay"))

# File "c:\Users\My_Sowriyam\eclipse-workspace\PythonInterviewProblems\Zoho-preparations\Error-Python.py", line 43, in <module>
#     print(int("Vijay"))
#           ^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'Vijay'

# -------------------------------------------------------------------------------------------------------------------------------------

# 6. Index Error -> Raised when an index of a sequence does not exist

# lst = [1,2,3,4,5]
# print(f'Lenght of list is {len(lst)}')
# print(f'10th value in a list is {lst[10]}')

# File "c:\Users\My_Sowriyam\eclipse-workspace\PythonInterviewProblems\Zoho-preparations\Error-Python.py", line 54, in <module>
# Lenght of list is 5
#     print(f'10th value in a list is {lst[10]}')
#                                      ~~~^^^^
# IndexError: list index out of range

# -------------------------------------------------------------------------------------------------------------------------------------

# 7. Key Error -? Raised when a key does not exist in a dictionary

# dic = {"Name" : "Vijay"}
# print(f"Vijay's Age is {dic["Age"]}")

# File "c:\Users\My_Sowriyam\eclipse-workspace\PythonInterviewProblems\Zoho-preparations\Error-Python.py", line 65, in <module>
#     print(f"Vijay's Age is {dic["Age"]}")
#                             ~~~^^^^^^^
# KeyError: 'Age'

# -------------------------------------------------------------------------------------------------------------------------------------

# 8. Zero Division Error -> Raised when the second operator in a division is zero

# print(5/0)
# File "c:\Users\My_Sowriyam\eclipse-workspace\PythonInterviewProblems\Zoho-preparations\Error-Python.py", line 73, in <module>
#     print(5/0)
#           ~^~
# ZeroDivisionError: division by zero

# -------------------------------------------------------------------------------------------------------------------------------------

# 9. Import Error -> Raised when an imported module does not exist

# from numpy import somethingstrange

# File "c:\Users\My_Sowriyam\eclipse-workspace\PythonInterviewProblems\Zoho-preparations\Error-Python.py", line 82, in <module>
#     from numpy import somethingstrange
# ImportError: cannot import name 'somethingstrange' from 'numpy' 

# -------------------------------------------------------------------------------------------------------------------------------------

# 10. Module Not Found Error -> It occurs when the interpreter cannot find the specified module in your code

# from calculator import *

# File "c:\Users\My_Sowriyam\eclipse-workspace\PythonInterviewProblems\Zoho-preparations\Error-Python.py", line 90, in <module>
#     from calculator import *
# ModuleNotFoundError: No module named 'calculator'

# -------------------------------------------------------------------------------------------------------------------------------------

# 11. Attribute Error -> Raised when the datatype has no attribute like string doesn't has push attribute.

# name = "Vijay"
# name.push("Swathi")
# print(name)

# File "c:\Users\My_Sowriyam\eclipse-workspace\PythonInterviewProblems\Zoho-preparations\Error-Python.py", line 99, in <module>
#     name.push("Swathi")
#     ^^^^^^^^^
# AttributeError: 'str' object has no attribute 'push'

# -------------------------------------------------------------------------------------------------------------------------------------

# 12. EOF Error -> It attempts to read data but encounters the end of the input stream without receiving any data just like ctrl + z

# n = int(input())
# print(n*10)

# ^Z 
# Traceback (most recent call last):
#   File "C:\Users\My_Sowriyam\eclipse-workspace\PythonInterviewProblems\Zoho-preparations\Error-Python.py", line 109, in <module>
#     n = int(input())
#             ^^^^^^^
# EOFError

# -------------------------------------------------------------------------------------------------------------------------------------

# 13. Overflow Error -> Raised when the result of a numeric calculation is too large

# import math
# print(math.exp(999))

# File "c:\Users\My_Sowriyam\eclipse-workspace\PythonInterviewProblems\Zoho-preparations\Error-Python.py", line 122, in <module>
#     print(math.exp(999))
#           ^^^^^^^^^^^^^
# OverflowError: math range error

# -------------------------------------------------------------------------------------------------------------------------------------