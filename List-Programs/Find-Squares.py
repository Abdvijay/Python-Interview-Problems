# Enter the list elements : 1 2 3 4 5
# [1, 4, 9, 16, 25]

lst = list(map(int,input("Enter the list elements : ").split()))
sq = [x*x for x in lst]
print(sq)