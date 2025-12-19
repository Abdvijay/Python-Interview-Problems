customer_transation = list(map(int,input("Enter the days transactions : ").split()))
predefind_limit = int(input("Enter the limit amount : "))
total_withdraw_amount = sum(customer_transation)
limit_status = ""
remaining_limit = predefind_limit - total_withdraw_amount

if total_withdraw_amount > predefind_limit:
    limit_status= "Limit Exceeded"
else:
    limit_status = "Within Limit"

print(f"Total Withdraw  = {total_withdraw_amount}")
print(f"Limit Status    = {limit_status}")
print(f"Remaining Limit = {remaining_limit}")

# Sample Input and Sample Output

# Enter the days transactions : 1200 1300 200 2300 5000
# Enter the limit amount : 7500
# Total Withdraw  = 10000
# Limit Status    = Limit Exceeded
# Remaining Limit = -2500

# Enter the days transactions : 1200 1300 200 2300     
# Enter the limit amount : 7500
# Total Withdraw  = 5000
# Limit Status    = Within Limit
# Remaining Limit = 2500