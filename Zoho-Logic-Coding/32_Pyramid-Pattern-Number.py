# 1. Right Angled Triangle
# *
# **
# ***
# ****
# *****

# rows = int(input("Enter the rows : "))
# for i in range(rows):
#     print((i+1) * "*")

# 2. Inverted Right Angled Triangle
# *****
# ****
# ***
# **
# *

# rows = int(input("Enter the rows : "))
# for i in range(rows):
#     count = rows - i
#     print("*" * count)

# or

# rows = 5
# for i in range(rows,0,-1):
#     print("*" * i)

# 3. Left Angled Trianled
#     *
#    **
#   ***
#  ****
# *****

# rows = int(input("Enter the rows : "))
# for i in range(1,rows+1):
#     print(" " * (rows - i) + "*" * i)

# 4.Inverted Left Angled Triangle
# *****
#  ****
#   ***
#    **
#     *
# rows = int(input("Enter the rows : "))
# for i in range(rows,0,-1):
#     print(" " * (rows - i) + "*" * i)

# 5. Pyramid Pattern
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * *

# rows = int(input("Enter the rows : "))
# for i in range(1,rows+1):
#     print(" " * (rows - i) + "* " * i)

# 6. Inverted Pyramid Pattern
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 

# rows = int(input("Enter the rows : "))
# for i in range(rows,0,-1):
#     print(" " * (rows - i) + "* " * i)

# 7. Diamond Pattern
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 

# rows = int(input("Enter the height of the pyramind (odd number only) : "))
# mid = rows + 1 // 2
# for i in range(1,mid+1):
#     print(" " * (mid - i) + "* " * i)
# for i in range(mid-1,0,-1):
#     print(" " * (mid - i) + "* " * i)

# 8. Hollow Square Pattern
# * * * * * 
# *       * 
# *       * 
# *       * 
# * * * * * 

# n = int(input("Enter the n value : "))
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print("*", end= " ")
#         else:
#             print(" ", end=" ")
#     print()

# 9. Hollow Right Angled Triangle
# * 
# * * 
# *   * 
# *     * 
# * * * * * 

# n  = int(input("Enter the n value : "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if i == j or i == n or j == 1:
#             print("*", end= " ")
#         else:
#             print(" ", end=" ")
#     print()