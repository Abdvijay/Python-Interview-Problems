# Important Points : 

# Definition of Exception Handling : 

#         Exception handling in Python provides a mechanism to manage runtime errors and unexpected events, 
# preventing program termination and allowing for graceful recovery.


# Keywords : 
#         1. try    -> a try block encloses code that might potentially raise an exception.
#         2. except -> a except block catches specific exceptions that occur within the try block.
#                      You can catch multiple specific exceptions or a general Exception type.
#                      Without try block you cannot use except.
#         3. else   -> The else block is executed if no exceptions occur within the try block.
#         4. finally-> The finally block always executes, regardless of whether an exception was raised or caught. 
#                      It is typically used for cleanup operations, such as closing files or releasing resources.
#         5. raise  -> The raise keyword allows you to manually raise an exception, either a built-in one or a custom exception.

a = int(input("Enter a value : "))
try:
    b = int(input("Enter b value : "))
    result = a / b
except ZeroDivisionError as e:
    print("Zero Division Error Raised -> You cannot divide by zero : ",e)
except ValueError as e:
    print("Value Error Raised -> Invalid input : ",e)
else:
    print(f'{a} / {b} is {result}')
finally:
    print("Program closed !!!")

# Enter a value : 5
# Enter b value : dsfd
# Value Error Raised -> Invalid input :  invalid literal for int() with base 10: 'dsfd'
# Program closed !!!

# Enter a value : 5
# Enter b value : 0
# Zero Division Error Raised -> You cannot divide by zero :  division by zero
# Program closed !!!

# Enter a value : 6
# Enter b value : 3
# 6 / 3 is 2.0
# Program closed !!!