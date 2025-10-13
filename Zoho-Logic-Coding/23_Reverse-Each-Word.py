# Sample Input
# Enter the sentence : i love you vijay

# Sample Output
# The reverse sentence of each word is : i evol uoy yajiv 

sentence = input("Enter the sentence : ").split()
rev = ""
for word in sentence:
    rev += word[::-1] + " "
print(f"The reverse sentence of each word is : {''.join(rev)}")