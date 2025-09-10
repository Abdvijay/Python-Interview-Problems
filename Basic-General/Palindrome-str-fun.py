# Enter the string : vijay
# The given string vijay is not a palindrome

if __name__ == '__main__':
    str = input("Enter the string : ")
    rev = str[::-1]
    if str == rev:
        print(f'The given string {str} is palindrome')
    else:
        print(f'The given string {str} is not a palindrome')