rows = 5
    
for i in range(1, rows + 1):
    # Calculate the starting number of the row (Triangular Number: 1, 3, 6, 10...)
    # Formula: i * (i + 1) / 2
    start_of_row = int(i * (i + 1) / 2)
    
    row_output = ""
    
    # Loop 'i' times (length of the row)
    for j in range(i):
        # Count down from the starting number
        num_to_print = start_of_row - j
        row_output += str(num_to_print) + " "
            
    print(row_output.strip())

# OUTPUT

# 1
# 3 2
# 6 5 4
# 10 9 8 7
# 15 14 13 12 11