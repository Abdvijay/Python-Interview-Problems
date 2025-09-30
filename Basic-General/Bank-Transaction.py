if __name__ == "__main__":
    print("! Welcome to Vijay's Bank !")
    status = True
    accounts = {}
    while status == True:
        print("# Please choose one option")
        print("1.Account Creation")
        print("2.Balance Check")
        print("3.Amount Deposit")
        print("4.Amount Withdraw")
        print("5.Exit")
        option = int(input("Enter your option as number : "))
        if option == 1:
            acc_number = int(input("Enter the account number (5 digits) : "))
            if acc_number not in accounts and len(str(acc_number)) == 5:
                acc_name = input("Enter the account holder name : ")
                initial_amount = int(input("Enter the initial amount : "))
                accounts[acc_number] = [acc_name,initial_amount]
            else:
                print("Sorry, already account number exists or your account number is incorrect !")
        elif option == 2:
            current_acc_number = int(input("Enter your 5 digit account number to check your balance : "))
            if current_acc_number in accounts and len(str(current_acc_number)) == 5:
                print(f"Your account number is {current_acc_number}")
                print(f"Your account holder name is {accounts[current_acc_number][0]}")
                print(f"Your balance amount is {accounts[current_acc_number][1]}")
                print("Thank you for visiting us !!!")
            else:
                print("Sorry, you entered account number is wrong or mismatch!")
                print("Please enter your correct account number :)")
        elif option == 3:
            current_acc_number = int(input("Enter your 5 digit acccount number : "))
            if current_acc_number in accounts and len(str(current_acc_number)) == 5:
                adding_amount = int(input("Enter your deposit amount : "))
                accounts[current_acc_number][1] += adding_amount
            else:
                print("Sorry, you entered account number is wrong or mismatch!")
                print("Please enter your correct account number :)")
        elif option == 4:
            current_acc_number = int(input("Enter your 5 digit account number : "))
            if current_acc_number in accounts and len(str(current_acc_number)) == 5:
                withdraw_amount = int(input("Enter your withdraw amount : "))
                if withdraw_amount <= accounts[current_acc_number][1]:
                    accounts[current_acc_number][1] -= withdraw_amount
                    print("Please collect your cash !!!")
                    print(f"Your remaining balance is {accounts[current_acc_number][1]}")
                else:
                    print("Your entered amount exceeds the balance amount so we declined your transaction !!!")
            else:
                print("Sorry, you entered account number is wrong or mismatch!")
                print("Please enter your correct account number :)")
        elif option == 5:
            status = False
        else:
            print("Please choose only one option (1,2,3,4,5)")
    print("Thank you for visiting Vijay's Bank !!!")
    print("Stay connected and enjoy your transaction :)")