from datetime import datetime


def format_date(date):
    return date.strftime('%m/%d/%y')


print(format_date(datetime.now()))
