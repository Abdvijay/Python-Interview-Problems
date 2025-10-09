from itertools import combinations
from itertools import permutations
from itertools import product
from itertools import cycle
from itertools import repeat
from itertools import takewhile
from itertools import dropwhile
from itertools import groupby

lst = ['A','B','C']

# Itertools Combinations
print("-----Combinations-----")
combos = combinations(lst,r=2)
for i in combos:
    print(i)
print("")

# Itertools Permutations
print("-----Permutations-----")
perm = permutations(lst,r=2)
for i in perm:
    print(i)
print("")

# Itertools product
print("-----Products-----")
lst1 = ['R','G','B']
lst2 = ['V','U','O']
products = product(lst1,lst2)
for i in products:
    print(i)
print("")

# Itertools cycle
print("-----Cycle-----")
lst_cycle = cycle(lst)
for _ in range(7):
    print(next(lst_cycle))
print("")

# Itertools cycle - traffic light
# import time
# signal_colors = ["Red","Yellow","Green"]
# color = cycle(signal_colors)
# for _ in range(5):
#     print(next(color))
#     time.sleep(2)
# print("")

# Itertools Repeat
print("-----Repeat-----")
for i in repeat(lst,4):
    print(i)
print("")

# Itertools Takewhile
print("-----Takewhile-----")
numbers = [-3,2,-5,6,-4]
numbers.sort()
neg = takewhile(lambda x:x < 0,numbers) # if condition is false then stop evaluating and return values as so far evalated
print(list(neg))
print("")

# Itertools Dropwhile
print("-----Dropwhile-----")
numbers = [-3,2,-5,6,-4]
numbers.sort()
non_neg = dropwhile(lambda x: x < 0,numbers) # if condition is false then stop evaluating and return values as so far evalated
print(list(non_neg))
print("")

# Itertools GroupBy
print("-----GroupBy-----")
print("Group By using Numbers")
numbers = [1,1,2,3,4,3,2,4,1,2]
numbers.sort()
grb = groupby(numbers)
for i,key in grb:
    print(i,"->",list(key))
    
print("\nGroup By using String len")
names = ["vijay","deeksha","raman","laksh","saranya"]
names.sort(key=lambda x:len(x))
grb = groupby(names,key=lambda x:len(x))
for i,key in grb:
    print(i,"->",list(key))
print("")

print("\nGroup By using Even or odd")
numbers = [12,34,14,11,55,66,33,44]
numbers.sort(key=lambda x: "even" if x % 2 == 0 else "odd")
grb = groupby(numbers,key=lambda x: "even" if x % 2 == 0 else "odd")
for i,key in grb:
    print(i,"->",list(key))
print("")

print("\nGroup By using custom key")
students = [
    {'name' : 'Vijay', 'age' : 24},
    {'name' : 'Swathi', 'age' : 23},
    {'name' : 'Laksh', 'age' : 19},
    {'name' : 'Dhiya', 'age' : 23},
    {'name' : 'Essai', 'age' : 24}
]
students.sort(key=lambda x:x["age"])
grb = groupby(students,key=lambda x:x["age"])
for i,key in grb:
    print(i,"age group ->",list(key))
print("")