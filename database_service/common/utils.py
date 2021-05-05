import datetime


def get_last_month() -> datetime.datetime:
    today = datetime.datetime.today()
    last_month = today - datetime.timedelta(days=30)
    return last_month
