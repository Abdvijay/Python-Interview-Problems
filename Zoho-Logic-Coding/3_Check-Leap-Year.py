# Sample Input
# Enter the year to check leap or not : 2000

# Sample Output
# The given year 2000 is Leap Year

year = int(input("Enter the year to check leap or not : "))
check_leap = lambda year : "Leap Year" if ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)) else "Not an Leap Year"
print(f"The given year {year} is {check_leap(year)}")