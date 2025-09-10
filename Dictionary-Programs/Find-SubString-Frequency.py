# Find substring frequency in a string using dictionary

# Input: string="abababa", substring="aba"
# Output: {'aba':3}

string = input("Enter the string : ")
sub_string = input("Enter the sub string : ")
result = {}
for i in range(0,len(string)):
    compare = string[i:i+len(sub_string)]
    if sub_string == compare and len(compare) == len(sub_string):
        if sub_string not in result:
            result[sub_string] = 1
        else:
            result[sub_string] = result[sub_string] + 1
print(result)