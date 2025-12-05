# Input:
# (a+b) * (c+d)

# Output:
# Balanced

# Input:
# (a+b)) + (c+d

# Output:
# Not Balanced

equation = input("Enter the equation to check balanced or not : ")
result = {'(' : 0,'[' : 0, '{' : 0}
flag = True

for i in equation:
    if i == '(':
        result['('] += 1
    elif i == '[':
        result['['] += 1
    elif i == '{':
        result['{'] += 1

    if i == ')':
        result['('] -= 1
    elif i == ']':
        result['['] -= 1
    elif i == '}':
        result['{'] -= 1
    
    if result['('] < 0 or result['['] < 0 or result['{'] < 0:
        flag = False
        break

if flag and result['('] == 0 and result['['] == 0 and result['{'] == 0:
    print(f'The equation {equation} is Balanced')
else:
    print(f'The equation {equation} is Not Balanced')

# Sample - 1:
# Enter the equation to check balanced or not : (a+b) + (c+d) 
# The equation (a+b) + (c+d) is Balanced

# Sample - 2:
# Enter the equation to check balanced or not : ((a+b) * c)   
# The equation ((a+b) * c) is Balanced

# Sample - 3:
# Enter the equation to check balanced or not : (a+b)) + (c+d
# The equation (a+b)) + (c+d is Not Balanced
                       
# Sample - 4:
# Enter the equation to check balanced or not : ((a+b) * (c-d)
# The equation ((a+b) * (c-d) is Not Balanced
              
# Sample - 5:
# Enter the equation to check balanced or not : (a+b] * {c+d} 
# The equation (a+b] * {c+d} is Not Balanced

# Sample - 6:
# Enter the equation to check balanced or not : {[a+(b*c)] + (d/e)}
# The equation {[a+(b*c)] + (d/e)} is Balanced

# Sample - 7:
# Enter the equation to check balanced or not : )(a+b)
# The equation )(a+b) is Not Balanced