# Question : Print the given year is Leap year or Not ?
# Concept : The year is a Leap year if it is divisible by 4 and not divisible by 100, or divisible by 400.

years = [2000,1998,2023,2009,2021]
for year in years:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f'Year : {year} is Leap Year')
    else:
        print(f'Year : {year} is Not an Leap Year')

# Sample Output : 

# Year : 2000 is Leap Year
# Year : 1998 is Not an Leap Year
# Year : 2023 is Not an Leap Year
# Year : 2009 is Not an Leap Year
# Year : 2021 is Not an Leap Year