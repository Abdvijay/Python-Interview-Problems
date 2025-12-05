# Input:
# "Abc@1234"

# Output:
# Strong Password

password = input("Enter the password : ")
length = len(password)
hasupper = any(ch.isupper() for ch in password)
haslower = any(ch.islower() for ch in password)
hasnumber = any(ch.isdigit() for ch in password)
hasspecial = any(not ch.isalnum() for ch in password)
if length >= 8:
    if haslower and hasupper and hasnumber and hasspecial:
        print(f'Your password {password} is Strong')
    else:
        print(f'Your password {password} is Weak')
else:
    print("Password must contain at least 8 characters")