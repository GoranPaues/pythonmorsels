def get_earliest(*dates):
    def get_date(date):
        month, day, year = date.split("/")
        return (year, month, day)
    return min(dates, key=get_date)