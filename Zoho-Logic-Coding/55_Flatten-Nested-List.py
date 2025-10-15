# Sample Input
# Enter the nested list : [1, [2,3], [4,[5]]]

# Sample Output
# After Flatterned [1, 2, 3, 4, 5]

import ast

def flatten_recursive(nested_list, flattened_list=None):
    if flattened_list is None: # First time only initialize empty list
        flattened_list = []
    for item in nested_list:
        if isinstance(item, list):
            flatten_recursive(item, flattened_list)
        else:
            flattened_list.append(item)
    return flattened_list

lst = ast.literal_eval(input("Enter the nested list : "))
print(f"After Flatterned {flatten_recursive(lst)}")