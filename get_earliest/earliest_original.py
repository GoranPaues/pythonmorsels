def get_earliest(date1, date2):
    date1_month, date1_day, date1_year = date1.split("/")
    date2_month, date2_day, date2_year = date2.split("/")
    if date1_year > date2_year:
        return date2
    elif date1_year < date2_year:
        return date1
    elif date1_month > date2_month:
        return date2
    elif date1_month < date2_month:
        return date1
    elif date1_day > date2_day:
        return date2
    elif date1_day < date2_day:
        return date1

    return date1