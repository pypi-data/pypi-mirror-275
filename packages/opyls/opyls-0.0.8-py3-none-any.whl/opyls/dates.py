import datetime


def full_date(date):
    return date.strftime("%Y-%m-%dT%H:%M:%SZ")


def full_date_now():
    return full_date(datetime.datetime.now())
