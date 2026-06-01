# Sample Input
# Enter the sentence : i love you vijay

# Sample Output
# The reverse sentence of each word is : i evol uoy yajiv 

sentence = input("Enter the sentence : ").split()
rev = ""
for word in sentence:
    rev += word[::-1] + " "
print(f"The reverse sentence of each word is : {''.join(rev)}")

# Another way to do the same is using map function as shown below

# sentence = list(map(str,input("Enter the sentence : ").split(" ")))
# temp = []
# for word in sentence:
#     temp.append(word[::-1])
# print(f"{(" ").join(temp)}")