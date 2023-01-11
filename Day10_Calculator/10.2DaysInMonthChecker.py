def is_leap(year):
    """Checks if input year is a leap year or not"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    """Returns the number of days in a month when number of the month and year are input"""
    leap_year = is_leap(year)
    if not leap_year:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        month_days= [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_days[month-1]

  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)