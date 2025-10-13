# Sample Input
# Enter the line count : 5

# Sample Output

#   *
#   **
#   ***
#   ****
#   *****

line = int(input("Enter the line count : "))
for i in range(1,line+1):
    print("*" * i)