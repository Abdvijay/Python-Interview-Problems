lst = list(map(int,input("Enter the list elements : ").split()))
logic = list(map(str,input("Enter the logic (ex : square,even,add 5,positive,divide 3): ").split()))
flag = True
if logic[0].lower() == "square":
    result = [n * n for n in lst]
elif logic[0].lower() == "even":
    result = [n for n in lst if n % 2 == 0]
elif logic[0].lower() == "add":
    result = [n + logic[1] for n in lst]
elif logic[0].lower() == "positive":
    result = [abs(x) for x in lst]
elif logic[0].lower() == "divide":
    result = [n // 2 for n in lst]
else:
    flag = False

if flag:
    print(result)
else:
    print("Invalid Logic")

# Enter the list elements : 1 2 3 
# Enter the logic (ex : square,even,add 5,positive,divide 3): square
# [1, 4, 9]

# Enter the list elements : 1 4 9
# Enter the logic (ex : square,even,add 5,positive,divide 3) : divide 3
# [0, 2, 4]

# Enter the list elements : 1 -2 4
# Enter the logic (ex : square,even,add 5,positive,divide 3): positive
# [1, 2, 4]

# Enter the list elements : 1 5 3 3
# Enter the logic (ex : square,even,add 5,positive,divide 3): even
# []