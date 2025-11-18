word = input("Enter the string to print : ").strip()
for i in range(0,len(word)):
    for j in range(0,i+1):
        print(word[j],end="")
    print("")

# OUTPUT

# Enter the string to print : PYTHON
# P
# PY
# PYT
# PYTH
# PYTHO
# PYTHON