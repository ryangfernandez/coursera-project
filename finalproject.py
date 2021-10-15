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
    #Exception if the month is 12, as the next month would be 1 of the next year, not 13.
    if month == 12: date1, date2 = datetime.date(year, month, 1), datetime.date(year+1, 1, 1)
    else: date1, date2 = datetime.date(year, month, 1), datetime.date(year, month+1, 1)
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

    #Checks if the given dates are valid using the is_valid_date() function.
    date1valid, date2valid = is_valid_date(year1, month1, day1), is_valid_date(year2, month2, day2)
 
    if (date1valid and date2valid):

        #Sets date1 and date2 to their corresponding dates, and calculates the difference in days.
        date1, date2 = datetime.date(year1, month1, day1), datetime.date(year2, month2, day2)
        difference = date2 - date1

        #If the difference is negative i.e. the second date is before the first date, 0 is returned.
        #If the difference is positive, then the number of days is returned.
        if difference.days > 0: return difference.days
        else: return 0
        
    else: return 0


def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day
      
    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid of if the input
      date is in the future.
    """

    #Sets today as the date when it is being run.
    #Uses days_between() to find the number of days between today and the date given.
    today = datetime.date.today()
    daydifference = days_between(year, month, day, today.year, today.month, today.day)
    return daydifference


