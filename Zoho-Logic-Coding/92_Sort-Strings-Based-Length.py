lst = list(map(str,input("Enter the list of strings : ").split()))
result = sorted(lst,key=len)
print(result)

# Sample Input and Sample Output

# Enter the list of strings : apple hi banana
# ['hi', 'apple', 'banana']

# Enter the list of strings : a abc ab
# ['a', 'ab', 'abc']

# Enter the list of strings : python is fun 
# ['is', 'fun', 'python']

# Enter the list of strings : one
# ['one']

# Enter the list of strings : aa b ccc
# ['b', 'aa', 'ccc']