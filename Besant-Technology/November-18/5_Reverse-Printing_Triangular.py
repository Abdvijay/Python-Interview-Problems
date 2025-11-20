rows = 4
    
for i in range(1, rows + 1):
    # Calculate the starting number of the row (Triangular Number: 1, 3, 6, 10...)
    # Formula: i * (i + 1) / 2
    start_of_row = int(i * (i + 1) / 2)
    
    # Run this loop using rows and print the start of row and reduce by one
    for j in range(i):
        print(start_of_row,end=" ")
        start_of_row -= 1
    print("")            

# OUTPUT

# 1
# 3 2
# 6 5 4
# 10 9 8 7
# 15 14 13 12 11