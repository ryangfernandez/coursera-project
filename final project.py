import datetime


def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month
    Returns:
      The number of days in the input month.
    """

    #Finds difference between the 1st of given month and the 1st of the next month.
    date1, date2 = datetime.date(year, month, 1), datetime.date(year, month+1, 1)

    difference = date2 - date1
    #Difference returns (days, seconds, microseconds), therefore only the number of days are called.
    return difference.days


def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day
      
    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    
    #Checks if all inputs are integers and if the year/month is valid: if not, return False.
    #Year and month checked before days since days_in_month functions requires valid arguments.
    intcheck = isinstance(year, int) and isinstance(month, int) and isinstance(day, int)
    yearcheck = (year >= datetime.MINYEAR) and (year <= datetime.MAXYEAR)
    monthcheck = (1 <= month <= 12)
    
    #Checks if the diven day is valid.
    if intcheck and yearcheck and monthcheck:
        
        daycheck = (1 <= day <= days_in_month(year, month))
        
        if daycheck: return True
        else: return False
        
    else: return False


def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date
      
    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is 
      before the first date.
    """

    date1valid, date2valid = is_valid_date(year1, month1, day1), is_valid_date(year2, month2, day2)

    if (date1valid and date2valid):

        date1, date2 = datetime.date(year1, month1, day1), datetime.date(year2, month2, day2)
        difference = date2 - date1

        if difference.days > 0: return difference.days
        else: return 0
        
    else: return 0
    

if __name__ == "__main__":
    print(days_between(2004, 6, 4, 2005, 1, 6))
