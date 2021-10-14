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

    # Creates a list of: leap years between datetime.MINYEAR and datetime.MAXYEAR,
    # months with 30 days and months with 31 days. If the month isn't in the list,
    # it is assumed to be February.
    leaps = [x for x in range(datetime.MINYEAR, datetime.MAXYEAR) if (x % 4) == 0]
    t_ones = [1, 3, 5, 7, 8, 10, 12]
    t_ies = [4, 6, 9, 11]

    # Defines date using the year and month given using a placeholder number of days as to not give an error.
    date = datetime.date(year, month, 1)

    if date.month in t_ones:
        return 31
    elif date.month in t_ies:
        return 30z
    else:
        if date.year in leaps:
            return 29
        else:
            return 28


if __name__ == "__main__":
    print(days_in_month(2015, 6))
