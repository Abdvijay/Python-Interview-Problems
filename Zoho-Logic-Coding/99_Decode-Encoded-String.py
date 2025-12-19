s = input("Enter the string : ")

stack = []
current_string = ""
current_number = 0

for ch in s:

    # If digit, build the number
    if ch.isdigit():
        current_number = current_number * 10 + int(ch)

    # If opening bracket, save state
    elif ch == '[':
        stack.append((current_string, current_number))
        current_string = ""
        current_number = 0

    # If closing bracket, decode
    elif ch == ']':
        prev_string, num = stack.pop()
        current_string = prev_string + current_string * num

    # If alphabet, add to current string
    else:
        current_string += ch

print(current_string)