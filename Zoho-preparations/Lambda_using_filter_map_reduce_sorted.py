from functools import reduce

#Lambda using multiple arguments
add = lambda a,b: a+b
print(f"Addition of 5 + 5 is {add(5,5)}")

#Lambda using multiple expression
calc = lambda a,b: (a+b,a-b,a*b,a/b)
add,sub,mul,div = calc(5,5)
print("Addition       of 5 + 5 is ",add)
print("Subtraction    of 5 - 5 is ",sub)
print("Multiplication of 5 * 5 is ",mul)
print("Division       of 5 / 5 is ",div)

#Lambda using map
numbers = [1,2,3,4,5]
squares = list(map(lambda x:x*x,numbers))
print(f"Original list : {numbers} -> Squares list : {squares}")

#Lambda using filter
numbers = [1,2,3,4,5]
odd = list(filter(lambda x:x%2 != 0,numbers))
print(f"Original list : {numbers} -> Odds List : {odd}")

#Lambda using reduce
numbers = [1,2,3,4,5]
product = reduce(lambda a,b:a*b,numbers)
print(f"Product of {numbers} -> {product}")

#Lambda using conditional statements
check_even = lambda x : "even" if x % 2 == 0 else "odd"
print(check_even(5))

#Lambda using sorted
names = ["vijay","deeksha","laksh","raman"]
names.sort(key=lambda x:len(x))
sort_names = sorted(names,key=lambda x:len(x))
print("Sorted names : ",sort_names)