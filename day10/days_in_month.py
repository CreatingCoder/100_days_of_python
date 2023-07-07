#return True or False value for whether it is a leap year, or not.
def leap_year(year):
    leap_year = True

    if(year%4 == 0):
        if(year%100 != 0 or year%400 ==0):
            leap_year = True        
    else:
        leap_year = False
        
    return leap_year

#return days in a month, calling the leap_year method to determine if it is a leap year or not
def days_in_month():
#30 days has September,
#April, June, and November.
#When short February's done
#All the rest have 31...
    
    month_days = {
        1 : 31,
        2 : 28, #29 in leap year
        3 : 31,
        4: 30,
        5 : 31,
        6 : 30,
        7 : 31,
        8 : 31,
        9 : 30,
        10 : 31,
        11 : 30,
        12 : 31
    }
    
    user_year = int(input('Please input a year: '))
    user_month = int(input('Please enter a month (1 - 12): '))
    is_leap_year = leap_year(user_year)
    
    if(is_leap_year):
        month_days[2] = 29
        
    return print(f'There are {month_days[2]} days in month {user_month} of {user_year}.')




days_in_month()

