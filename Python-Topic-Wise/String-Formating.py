# Definition - String formatting means inserting variables or values into strings in a readable and organized way.

# Three Ways : 

#   1. f - Strings  - Modern and fast and recommended
#   2. format()     - flexible and readable
#   3. % formatting - Older C style and less preferred

name = "Vijay"
age = 24
price = 86.382382
student = {name : "Vijay",age : 24}

print(f"1. Basic Variable Insertion Using (f-string way) : Name is {name}, Age is {age}, Price is {price}")
print(f"2. Inline Expression        Using (f-string way) : Sum is {6 + 3}, Diff is {6 - 3}")
print(f"3. Float Formatting         Using (f-string way) : Price of the item is {price:.2f}")
print(f"4. String Alignment         Using (f-string way) : |{name:<10}|{name:^10}|{name:>10}")
print(f"5. Using in Dictionary      Using (f-string way) : Student name is {student[name]} and his age is {student[age]}")
print("6. Basic Formatting         Using (format() way) : My name is {} and age is {}".format(name,age))
print("7. Positional Index         Using (format() way) : My name is {0} and his age is {1}".format(name,age))
print("8. Keyword Arguments        Using (format() way) : My name is {n} and age is {a}".format(a=age,n=name))
print("9. Float Formatting         Using (format() way) : Price of the item is {:.2f}".format(price))
print("10. Alignment and Padding   Using (format() way) : |{:<10}|{:^10}|{:>10}".format("Left","Center","Right"))
print("11. Basic Substitution      Using (%% formatting) : My name is %s and My age is %d" % (name,age))
print("12. Float Formatting        Using (%% formatting) : Price of the item is %.2f" % price)
print("13. Multiple Values         Using (%% formatting) : x = %d, y = %.2f, z = %s" % (10,34.43543,"Vijay"))
print("14. Percentage sign print   Using (% formatting) : use %% to print %")
print("15. String Alignement       Using (%% formatting) : |%-10s|%10s|" % ("Python","Vijay"))

# Output

# 1. Basic Variable Insertion Using (f-string way) : Name is Vijay, Age is 24, Price is 86.382382
# 2. Inline Expression        Using (f-string way) : Sum is 9, Diff is 3
# 3. Float Formatting         Using (f-string way) : Price of the item is 86.38
# 4. String Alignment         Using (f-string way) : |Vijay     |  Vijay   |     Vijay
# 5. Using in Dictionary      Using (f-string way) : Student name is Vijay and his age is 24
# 6. Basic Formatting         Using (format() way) : My name is Vijay and age is 24
# 7. Positional Index         Using (format() way) : My name is Vijay and his age is 24
# 8. Keyword Arguments        Using (format() way) : My name is Vijay and age is 24
# 9. Float Formatting         Using (format() way) : Price of the item is 86.38
# 10. Alignment and Padding   Using (format() way) : |Left      |  Center  |     Right
# 11. Basic Substitution      Using (% formatting) : My name is Vijay and My age is 24
# 12. Float Formatting        Using (% formatting) : Price of the item is 86.38
# 13. Multiple Values         Using (% formatting) : x = 10, y = 34.44, z = Vijay
# 14. Percentage sign print   Using (% formatting) : use %% to print %
# 15. String Alignement       Using (% formatting) : |Python    |     Vijay|