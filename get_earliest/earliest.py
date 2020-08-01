def get_earliest(date1, date2):
    date1_month = date1[:2]
    date1_day = date1[3:5]
    date1_year = date1[6:]
    date2_month = date2[:2]
    date2_day = date2[3:5]
    date2_year = date2[6:]
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