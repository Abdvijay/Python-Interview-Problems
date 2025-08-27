expression = input("Enter the expression with paranthesis : ")
openPara, closePara = 0, 0
for char in expression:
    if char == '(':
        openPara += 1
    elif char == ')':
        closePara += 1
if openPara == closePara:
    print(f'The expression {expression} is perfectly balanced.')
else:
    print(f'The expression {expression} is not an perfectly balanced.')