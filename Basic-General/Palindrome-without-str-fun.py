if __name__ == '__main__':
    str = input("Enter the string : ")
    rev = ''
    for i in range(len(str)-1,-1,-1):
        rev += str[i]
    if str == rev:
        print(f'The given string {str} is palindrome')
    else:
        print(f'The given string {str} is not a palindrome')