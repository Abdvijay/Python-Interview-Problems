# Enter the sentence separated by space : hi vijay how are you
# Total words count is :  5

sentence = list(input("Enter the sentence separated by space : ").split())
count = 0
for word in sentence:
    count += 1
print("Total words count is : ",count)