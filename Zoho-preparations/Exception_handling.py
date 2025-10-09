a = int(input("Enter a value : "))
try:
    b = int(input("Enter b value : "))
    print(a/b)
except ZeroDivisionError as e:
    print("You cannot divide by zero : ",e)
except ValueError as e:
    print("Invalid input : ",e)
finally:
    print("Program closed !!!")