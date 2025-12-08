from itertools import permutations

# lst = list(map(str,input("Enter the list elements : ").split()))
# r_value = int(input("Enter the value : "))
# result = permutations(lst,r=r_value)
# for perm in result:
#     print(perm)

# Output with itertools permutations

# ('A', 'B')
# ('A', 'C')
# ('B', 'A')
# ('B', 'C')
# ('C', 'A')
# ('C', 'B')

# Generalized permutations without itertools

def generate_permutations(lst, r):
    n = len(lst)
    result = []
    used = [False] * n  # Track which indices are already used in current permutation

    def backtrack(current):
        # If current permutation length == r, store a copy
        if len(current) == r:
            result.append(current.copy())
            return
        
        # Try adding each unused element
        for i in range(n):
            if not used[i]:
                used[i] = True           # mark as used
                current.append(lst[i])   # choose
                backtrack(current)       # explore
                current.pop()            # undo choice
                used[i] = False          # unmark

    # Edge case: not enough elements
    if n < r:
        return None

    backtrack([])
    return result


# --------- Main Program ---------
lst = list(map(str, input("Enter the list elements : ").split()))
r = int(input("Enter the r value : "))

perms = generate_permutations(lst, r)

if perms is None:
    print("Impossible")
else:
    for p in perms:
        print(p)