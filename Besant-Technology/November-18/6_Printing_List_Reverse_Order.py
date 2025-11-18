lst = [10,20,30,40,50]
for i in range(len(lst)-1,-1,-1):
    print(lst[i])
print("")
# Another Method
lst = [10,20,30,40,50]
rev_lst = reversed(lst)
print(f"Reversed List : {list(rev_lst)}")

# OUTPUT

# 50
# 40
# 30
# 20
# 10

# Reversed List : [50, 40, 30, 20, 10]