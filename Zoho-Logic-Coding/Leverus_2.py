outstanding_loan_balance = int(input("Enter the outstanding loan balance : "))
minimum_monthly_repayment = int(input("Enter the minimum monthly repayment : "))
maximum_allowed_repayment = int(input("Enter the maximum allowed repayment : "))

repayment_amount = int(input("Enter the repayment amount : "))
validation_status = "Invalid"
new_outstanding_balance = 0
more_than = False
if repayment_amount > outstanding_loan_balance:
    validation_status = "Invalid"
    reason = "Below minimum repayment amount"
    more_than = True
else:
    if repayment_amount < maximum_allowed_repayment:
        if repayment_amount > minimum_monthly_repayment:
            validation_status = "Valid"
            new_outstanding_balance = outstanding_loan_balance - repayment_amount

print(f"Repayment  Amount : {repayment_amount}")
print(f"Validation Status : {validation_status}")

if more_than:
    print(f"Reason            : {reason}")
else:
    print(f"New Outstanding Balance : {new_outstanding_balance}")

# Sample Input and Sample Output

# Enter the outstanding loan balance : 48000
# Enter the minimum monthly repayment : 5000
# Enter the maximum allowed repayment : 50000
# Enter the repayment amount : 18000
# Repayment  Amount : 18000
# Validation Status : Valid
# New Outstanding Balance : 30000

# Enter the outstanding loan balance : 48000
# Enter the minimum monthly repayment : 5000
# Enter the maximum allowed repayment : 50000
# Enter the repayment amount : 50000
# Repayment  Amount : 50000
# Validation Status : Invalid
# Reason            : Below minimum repayment amount